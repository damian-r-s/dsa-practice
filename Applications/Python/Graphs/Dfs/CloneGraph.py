# 133. Clone Graph
# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.nodes = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        if node.val in self.nodes:
            return self.nodes[node.val]

        newNode = Node(node.val)
        self.nodes[newNode.val] = newNode

        for n in node.neighbors:
            newNode.neighbors.append(self.cloneGraph(n))

        return newNode