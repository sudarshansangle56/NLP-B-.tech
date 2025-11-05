tree={
    'a':['b','c'],
    'b':['d', 'e'],
    'c':['f','g'],
    'd':['',''],
    'e':['',''],
    'f':['',''],
    'g':['',''],
}
print(tree)

from collections import deque

def bfs(tree, start):
    vis=[]
    queue= deque([start])

    while queue:
        node=queue.popleft()
        if node != '' and node not in vis:
            vis.append(node)
            children = tree.get(node,[])
            for child in children:
                if child != '':
                    queue.append(child)
    return vis

print("BFS Traversal:", bfs(tree, 'a'))