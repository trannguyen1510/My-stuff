import Puzzle
import Node
import searches
import sys

size = input("Enter puzzle's size: ")
try:
    puz = Puzzle.BasePuzzle(int(size))
except:
    print("Input Error !!!")
    sys.exit()

print("Enter puzzle: ")
puz.puzzle = puz.getPuzzle()
if not puz.checkPuzzle:
    print("Wrong input !!!")
    sys.exit()

print("Enter goal: ")
goal = Puzzle.BasePuzzle(int(size))
goal.puzzle = goal.getPuzzle()
if not puz.checkPuzzle:
    print("Wrong input !!!")
    sys.exit()

se = searches.Search(puz)
result = se.AStar(goal)
if not result:
    print("The input puzzle and the goal are the same. Do nothing!")
else:
    if type(result) == list:
        for index, node in enumerate(result):
            node.state.printPuzzle()
            if index != result.__len__() - 1:
                print(' ||')
                print(' ||')
                print(' ||')
                print('\  /')
                print(' \/')
    else:
        print(result)
