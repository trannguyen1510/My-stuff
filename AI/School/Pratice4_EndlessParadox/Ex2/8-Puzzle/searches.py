import Node
import Puzzle
from copy import deepcopy

class Search:
    def __init__(self, puz):
        self.node = Node.Node(puz)

    def FVal(self, node, goal):
        return node.depth + node.wrongTitles(goal)

    def MinF(self, frontier, goal):
        minF = frontier[0]
        for node in frontier:
            if self.FVal(node, goal) < self.FVal(minF, goal):
                minF = node
        return minF

    def FindPath(self, closed, tree_node, path):
        if tree_node.goalState(self.node.state):
            path.insert(0, tree_node)
            return path
        if tree_node in closed:
            path.insert(0, tree_node)
            current = tree_node.parent
            if current:
                self.FindPath(closed, current, path)
        return False

    def AStar(self, goal):
        closed = []
        frontier = [self.node]
        while frontier:
            tree_node = self.MinF(frontier, goal)
            closed.append(tree_node)
            frontier.remove(tree_node)
            if tree_node.goalState(goal):
                closed.append(tree_node)
                break
            for child in tree_node.generateChild():
                if child in frontier:
                    if child.depth > tree_node.depth + 1:
                        child.parent = tree_node
                        frontier.append(child)
                else:
                    child.parent = tree_node
                    frontier.append(child)
        path = []
        self.FindPath(closed, tree_node, path)
        for node in path:
            if node.goalState(self.node.state):
                return path
        return "There is no path to the goal"
