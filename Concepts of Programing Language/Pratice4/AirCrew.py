import tkinter as tk
from tkinter import filedialog
import sys

# Idea:
# - To minimize the money to pay to the crew, the subtraction of money to pay between main position and sub position
#   need to be max. Then, when choosing sub pilot position, the money to pay will maximally be reduced
# - The sub pilot need the maximum subtractions so the main pilot will be the minimum subtractions
# - The main pilot has no less flight hours then the sub pilot so when choosing pair, the main position has higher index
#   to sub position in list
# - And because of that, sub position cannot be the last value in list (or need to have a value has higher index to pair
#   with)
# - When having all paired, the result will be sum of the money to pay to all pairs

root = tk.Tk()
root.withdraw()
target = filedialog.askopenfile(title='Select input file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
if not target or not target.name.lower().endswith('.txt'):
    print('Input errors. Pleas choose an appropriate file!')
    sys.exit()

with open(target.name, 'r') as file:        # get input from AirCrew_IN.txt
    input_list = file.read().splitlines()

index = 0
# def readinput():            # function to get the next value in input_list with each time it' s called
#     global input_list
#     global index
#     i = index
#     index += 1
#     return input_list[i]


def custom_subtraction(input_str):
    val = input_str.split(" ")
    return int(val[0]) - int(val[1])            # subtraction


pilot_num = int(input_list[0])
input_list.pop(0)

sum_salary = 0
n = len(input_list)
while n > 0:        # end when there are no pilots left
    max_val = 0
    min_val = 10000
    i_max = 0
    i_min = 0
    for i, val in enumerate(input_list):
        if max_val < custom_subtraction(val):
            if i != n - 1:
                max_val = custom_subtraction(val)
                i_max = i
        if min_val > custom_subtraction(val):
            if i_min > i_max:
                min_val = custom_subtraction(val)
                i_min = i
            else:
                i_min += 1
    sub_position = input_list[i_max].split(" ")
    sum_salary += int(sub_position[1])   # pick sub aircrew
    main_position = input_list[i_min].split(" ")
    sum_salary += int(main_position[0])    # pick main aircrew
    input_list.pop(i_min)       # remove i_min first cause i_min > i_max
    input_list.pop(i_max)       # if remove i_max first, the i_min would change
    n_old = n
    n = len(input_list)     # while continuation's condition
    if n == n_old:          # check if while can continue
        print('Cannot pick a pair of aircrews!!')
        sys.exit()
print(sum_salary)

root = tk.Tk()
root.withdraw()
target = filedialog.askopenfile(title='Select input file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
if not target or not target.name.lower().endswith('.txt'):
    print('Input errors. Pleas choose an appropriate file!')
    sys.exit()

with open(target.name, 'w') as file:    # write result to AirCrew_OUT.txt
    file.write(str(sum_salary))


