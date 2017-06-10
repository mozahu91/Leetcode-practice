"""
Implementation of Depth-First Search
This algorithm we will be discussing is Depth-First search which as the name hints at, explores possible vertices (from a supplied root) down each branch before backtracking. This property allows the algorithm to be implemented succinctly in both iterative and recursive forms. Below is a listing of the actions performed upon each visit to a node.

Mark the current vertex as being visited.
Explore each adjacent vertex that is not included in the visited set.
We will assume a simplified version of a graph in the following form:
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
         
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

dfs(graph, 'A') 


#Recursively it can be written by:

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for nxt in graph[start] - visited:
        dfs(graph, nxt, visited)
    return visited

dfs(graph, 'A') 



ef dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for nxt in graph[vertex] - set(path):
            if nxt == goal:
                yield path + [nxt]
            else:
                stack.append((nxt, path + [nxt]))

list(dfs_paths(graph, 'A', 'F'))
         
