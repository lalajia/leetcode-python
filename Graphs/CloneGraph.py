"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}
 

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Input: adjList = [[2],[1,3],[2]]

Output: [[2],[1,3],[2]]


"""

from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # Dictionary to store the mapping of original node to its clone
        oldToNew = {}

        # Define a helper function `dfs` to perform depth-first traversal
        def dfs(node):
            # If the current node is already cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # Create a copy/clone of the current node with its value
            copy = Node(node.val)

            # Map the original node to the cloned node
            oldToNew[node] = copy

            # Recursively clone all the neighbors of the current node
            for nei in node.neighbors:
                # Add the cloned neighbors to the neighbors list of the cloned node
                copy.neighbors.append(dfs(nei))

            # Return the clone of the current node
            return copy

        # If the input node is None, return None (empty graph)
        # Otherwise, start the cloning process from the given node
        return dfs(node) if node else None


# node1 = Node(1)
# node1.neighbors = Node(2)
# node1.neighbors.neighbors = Node(3)
# node1.neighbors.neighbors = Node(4)
# node1.neighbors.neighbors.neighbors = node1


def build_graph(adj_list):
    if not adj_list:
        return None

    nodes = {}
    for i in range(len(adj_list)):
        nodes[i + 1] = Node(i + 1)

    for i, neighbors in enumerate(adj_list):
        nodes[i + 1].neighbors = [nodes[nei] for nei in neighbors]

    return nodes[1]  # Return the starting node


adj_list = [[2], [1, 3], [2]]

# Build the graph
original_graph = build_graph(adj_list)

print(Solution().cloneGraph(original_graph))
