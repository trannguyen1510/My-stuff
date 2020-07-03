import networkx as nx
import matplotlib as plt
import sys


def Visit(G,root, path, closed, max_depth):
    path.append(root)
    closed.append(root)
    if max_depth < 0:
        return False
    for child in G.neighbors(root):
        if child not in closed:
            Visit(G,child,path,closed,max_depth-1)
    return path


def IDDFS_Visit(G,root,max_depth):
    path = []
    for i in range(max_depth):
        closed = []
        Visit(G, root, path, closed, i)
    return path

def Search(G, path, goal, closed, max_depth):
    current = path[-1]
    if current == goal:
        return path
    closed.append(current)
    if max_depth <= 0:
        return False
    for child in G.neighbors(current):
        if child not in closed:
            new_path = list(path)
            new_path.append(child)
            result = Search(G,new_path,goal,closed,max_depth-1)
            if result:
                return result
    return False


def IDDFS_Search(G,root, goal, max_depth):
    closed = []
    for i in range(0, max_depth):
        result = Search(G, [root], goal, closed, max_depth)
        if result:
            return result
    return 'There is no goal or path to goal or not enough depth'


def Graph_Visit(G, root, Type, max_depth = 0):
    node = root
    closed = []
    open = [node]
    path = []
    while open:
        if Type == 2:           #Depth-First Search
            node = open.pop(0)
            if node not in closed:
                temp = []
                for child in nx.neighbors(G, node):
                    temp.append(child)
                open = temp + open
                path.append(node)
        else:
            if Type == 1:       #Breadth-First Search
                node = open.pop(0)
                if node not in closed:
                    for child in nx.neighbors(G, node):
                        open.append(child)
                    path.append(node)
            else:
                if Type == 3:   #Iterative Deepening Depth First Search
                    return IDDFS_Visit(G,root,max_depth)
                else:
                    print('There is no such type !')
                    sys.exit()
        closed.append(node)
    return path


def Graph_Search(G, root, goal, Type, max_depth = 0):
    node = root
    closed = []
    queue = [[node]]
    if (root == goal):
        print('goal state is root state')
        sys.exit()
    while queue:
        if Type == 2:               #Depth-First Search
            path = queue.pop(0)
            node = path[-1]
            if node not in closed:
                temp = []
                for child in nx.neighbors(G, node):
                    new_path = list(path)
                    new_path.append(child)
                    if child == goal:
                        return new_path
                    temp.append(new_path)
                queue = temp + queue
        else:
            if Type == 1:           #Breadth-First Search
                path = queue.pop(0)
                node = path[-1]
                if node not in closed:
                    for child in nx.neighbors(G, node):
                            new_path = list(path)
                            new_path.append(child)
                            if child == goal:
                                return new_path
                            queue.append(new_path)
            else:
                if Type == 3:           #Iterative Deepening Depth First Search
                    return IDDFS_Search(G,root,goal,max_depth)
                else:
                    print('There is no such type !')
                    sys.exit()
        closed.append(node)
    return "There is no goal or path to goal"

#Main
G = nx.Graph()
print('0: Visit', '1: Search')
try:
    mode = int(input('Enter mode: ').strip())       # mode is an interger number
except:
    print('Input error !!!')
    sys.exit()
print("Enter data:")
while True:
    i = input()
    if i == "exit":
        break
    else:
        i = i.split(",")
        if i.__len__() != 2:
            print("Input Error!")
            sys.exit()
    G.add_edge(i[0].strip(), i[1].strip())
if mode:
    root = input('Root: ').strip()
    goal = input('Goal: ').strip()
    print('1: Breadth-First Search', '2: Depth-First Search', '3: Iterative Deepening Depth First Search')
    try:
        Type = int(input('Type of search: ').strip())      # Type is an interger number
    except:
        print('Input error !!!')
        sys.exit()
    if root not in G.nodes:
        print("There is no root state!")
        sys.exit()
    if goal not in G.nodes:
        print("There is no goal state!")
        sys.exit()
    if Type == 3:
        try:
            max_depth = int(input('Depth: ').strip())     # dept is an interger number
        except:
            print('Input error !!!')
            sys.exit()
        path = Graph_Search(G, root, goal, Type, max_depth)
    else:
        path = Graph_Search(G, root, goal, Type)
else:
    root = input('Root: ').strip()
    print('1: Breadth-First Search', '2: Depth-First Search', '3: Iterative Deepening Depth First Search')
    try:
        Type = int(input('Type of search: ').strip())  # Type is an interger number
    except:
        print('Input error !!!')
        sys.exit()
    if root not in G.nodes:
        print("There is no root state!")
        sys.exit()
    if Type == 3:
        try:
            max_depth = int(input('Depth: ').strip())     # dept is an interger number
        except:
            print('Input error !!!')
            sys.exit()
        path = Graph_Visit(G, root, Type, max_depth)
    else:
        path = Graph_Visit(G,root,Type)
print(path)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=2500, font_size=8)
plt.show()