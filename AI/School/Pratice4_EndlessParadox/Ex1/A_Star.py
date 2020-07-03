import sys
import networkx as nx

G = nx.Graph()
print('Enter data:')
try:
    while True:
        data = input().strip()
        if data != 'exit':
            data = data.split(',')
            G.add_edge(data[0].strip(), data[1].strip(), distance=int(data[2].strip()))
        else:
            break
except:
    print('Wrong input !!!')
    sys.exit()

print('Enter skyway from cities to the goal:')
try:
    while True:
        data = input().strip()
        if data != 'exit':
            data = data.split(',')
            G.nodes[data[0].strip()]['skyway'] = int(data[1].strip())
            G.nodes[data[0].strip()]['pre'] = None
        else:
            break
except:
    print('Wrong input !!!')
    sys.exit()

root = input('Enter start city: ').strip()
if root not in G.nodes:
    print('There is no above city !')
    sys.exit()
goal = input('Enter goal city: ').strip()
if goal not in G.nodes:
    print('There is no above city !')
    sys.exit()


def MinF(G, frontier):
    minF = G.nodes[frontier[0]]['total']
    Node = frontier[0]
    for node in frontier:
        data = G.nodes[node]['total']
        if data < minF:
            minF = data
            Node = node
    return Node

def FindPath(G, closed, root, goal, path):
    if goal == root:
        path.insert(0, goal)
        return path
    if goal in closed:
        path.insert(0, goal)
        current = G.nodes[goal]['pre']
        if current:
            FindPath(G, closed, root, current, path)


def A_Star(G, root, goal):
    closed = []
    frontier = [root]
    G.nodes[root]['cost'] = 0
    G.nodes[root]['total'] = 0
    while frontier:
        Node = MinF(G, frontier)
        closed.append(Node)
        frontier.remove(Node)
        if Node == goal:
            closed.append(goal)
            break
        for adjacent in G.neighbors(Node):
            if adjacent not in closed:
                if adjacent in frontier:
                    if G.nodes[adjacent]['cost'] > G.nodes[Node]['cost'] + G[Node][adjacent]['distance']:
                        G.nodes[adjacent]['cost'] = G.nodes[Node]['cost'] + G[Node][adjacent]['distance']
                        G.nodes[adjacent]['total'] = G.nodes[adjacent]['cost'] + G.nodes[adjacent]['skyway']
                        G.nodes[adjacent]['pre'] = Node
                        frontier.append(adjacent)
                else:
                    G.nodes[adjacent]['cost'] = G.nodes[Node]['cost'] + G[Node][adjacent]['distance']
                    G.nodes[adjacent]['total'] = G.nodes[adjacent]['cost'] + G.nodes[adjacent]['skyway']
                    G.nodes[adjacent]['pre'] = Node
                    frontier.append(adjacent)
    path = []
    FindPath(G, closed, root, goal, path)
    if root in path:
        return path
    else:
        return 'There is no path to the goal'


result = A_Star(G, root, goal)
print(result)