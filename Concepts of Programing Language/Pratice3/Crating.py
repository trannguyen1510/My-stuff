import tkinter as tk
from tkinter import filedialog
import sys

# Ideas:
# A rectangular need at least 3 pair of equal edges with one each of a rectangle

root = tk.Tk()
root.withdraw()
target = filedialog.askopenfile(title='Select input file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
if not target or not target.name.lower().endswith('.txt'):
    print('Input errors. Pleas choose an appropriate file!')
    sys.exit()

with open(target.name, 'r') as file:        # get input from Box_IN1.txt or Box_IN2.txt
    input_list = file.read().splitlines()


def check_crate(input_list):
    for val in input_list:
        val_list = val.split(" ")
        first = sum(val_list[0] in s for s in input_list)
        second = sum(val_list[1] in s for s in input_list)
        if val_list[0] != val_list[1]:  # if a surface is rectangle
            if first != 4 or second != 4:
                return False
            if first == 6 or second == 6:
                return False
        else:                           # if a surface is square
            if first != 8 or second != 8:
                return False
    return True


root = tk.Tk()
root.withdraw()
target = filedialog.askopenfile(title='Select input file', filetypes=(('Text files', '*.txt'), ('All files', '*.*')))
if not target or not target.name.lower().endswith('.txt'):
    print('Input errors. Pleas choose an appropriate file!')
    sys.exit()
result = check_crate(input_list)
with open(target.name, 'w') as file:    # write result to Box_OUT.txt
    if result:
        print("YES")
        file.write("YES")
    else:
        print("NO")
        file.write("NO")
