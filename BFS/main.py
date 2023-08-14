from collections import defaultdict
from collections import deque


class Graph:

    # constructor
    def __init__(self, vertices):
        # default dictionary to store graph
        self.graph = defaultdict(list)
        self.V = vertices

    # function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # function to print a BFS of the graph
    def BFS(self, s):
        """Time Complexity: O(V+E), where V is the number of nodes and E is the number of edges.
        Auxiliary Space: O(V)"""
        # mark all vertices as not visited
        # assuming each vertex is an int and start from 0 -> get max key + 1 -> total_vertex
        visited = [False] * (max(self.graph) + 1)
        # create a queue for BFS
        q = deque()
        # marked the source node as visited and enqueue it
        q.append(s)
        visited[s] = True
        while q:
            s = q.popleft()
            print(s, end=" ")
            # get all adjacent vertices of the dequeued vertex s
            # if an adjacent node has not been visited, then marked visited and enqueue it
            for i in self.graph[s]:
                if visited[i] is False:
                    q.append(i)
                    visited[i] = True

    """DFS (Depth-First Search) for Graph algorithm:
    Create a recursive function that takes the index of the node and a visited array 
    -> input: a index representing the start and a visited array for once traverse only
    1. Marked the current node as visited and print the node
    2. Traverse all the adjacent and unmarked nodes and call the recursive function with the index of adjacent node
    """
    """Time Complexity: O(V+E), where V is the number of nodes and E is the number of edges.
       Auxiliary Space: O(V)"""
    # recursive function for DFS
    def DFSUtil(self, v, visited):
        # marked the node as visited and print it
        visited.add(v)
        print(v, end=' ')
        # call recursive function to adjacent node if it is not visited
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.DFSUtil(neighbor, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

    # A recursive function used by topologicalSort
    def TopologicalSortUtil(self, v, visited, stack):
        # mark curr node as visited
        visited[v] = True
        # call recursive function to adjacent node if it is not visited:
        for neighbor in self.graph[v]:
            if visited[neighbor] is False:
                self.TopologicalSortUtil(neighbor, visited, stack)
        # push current index to stack which store index
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # marked all node as not visited
        visited = [False] * self.V
        stack = []
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] is False:
                self.TopologicalSortUtil(i, visited, stack)
        print(stack[::-1])


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")

# Function Call
g.topologicalSort()








