

class BasePuzzle:
    def __init__(self, size):
        self.size = size
        self.puzzle = []
        self.blank = (0, 0)
        self.moves = ["U", "D", "L", "R"]

    def getPuzzle(self):
        puz = []
        for i in range(0, self.size):
            temp = input().split(" ")
            puz.append(temp)
            for j, val in enumerate(temp):
                if val == "_":
                    self.blank = (i, j)
        return puz

    def checkPuzzle(self):
        for obj in self.puzzle:
            if obj.length != self.size - 1:
                return False
        return True

    def checkGoal(self, goal):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if self.puzzle[i][j] != goal.puzzle[i][j]:
                    return False
        return True

    def swap(self, x1, y1, x2, y2):
        temp = self.puzzle[x1][y1]
        self.puzzle[x1][y1] = self.puzzle[x2][y2]
        self.puzzle[x2][y2] = temp

    def up(self):
        if self.blank[0] != 0:
            self.swap(self.blank[0], self.blank[1], self.blank[0] - 1, self.blank[1])
        self.blank = (self.blank[0] - 1, self.blank[1])

    def down(self):
        if self.blank[0] != self.size - 1:
            self.swap(self.blank[0], self.blank[1], self.blank[0] + 1, self.blank[1])
            self.blank = (self.blank[0] + 1, self.blank[1])

    def left(self):
        if self.blank[1] != 0:
            self.swap(self.blank[0], self.blank[1], self.blank[0], self.blank[1] - 1)
            self.blank = (self.blank[0], self.blank[1] - 1)

    def right(self):
        if self.blank[1] != self.size - 1:
            self.swap(self.blank[0], self.blank[1], self.blank[0], self.blank[1] + 1)
            self.blank = (self.blank[0], self.blank[1] + 1)

    def printPuzzle(self):
        for i in range(0, self.size):
            for j in range(0, self.size):
                if j == self.size -1:
                    print(self.puzzle[i][j])
                else:
                    print(self.puzzle[i][j], end=" ")

    def doMove(self, move):
        if move == "U":
            self.up()
        if move == "D":
            self.down()
        if move == "L":
            self.left()
        if move == "R":
            self.right()
