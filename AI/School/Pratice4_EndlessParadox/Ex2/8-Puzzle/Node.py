from copy import deepcopy

class Node:
    def __init__(self, puzzle, parent=None, move=""):
        self.state = puzzle
        self.parent = parent
        if parent is None:
            self.depth = 0
            self.moves = move
        else:
            self.depth = parent.depth + 1
            self.moves = parent.moves + move

    def goalState(self, goal):
        return self.state.checkGoal(goal)

    def generateChild(self):
        children = []
        for move in self.state.moves:
            new_state = deepcopy(self.state)
            new_state.doMove(move)
            if new_state.blank is not self.state.blank:
                children.append(Node(new_state, self, move))
        return children

    def wrongTitles(self, goal):
        count = 0
        for i in range(0, self.state.size):
            for j in range(0, self.state.size):
                if self.state.puzzle[i][j] != goal.puzzle[i][j]:
                    count += 1
        return count
