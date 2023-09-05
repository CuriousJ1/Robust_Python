'''
Version 1.

'''

from collections import defaultdict
from typing import Generic, TypeVar

Node = TypeVar("Node")
Edge = TypeVar("Edge")
# directed graph
class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges: dict[Node, list[Edge]] = defaultdict(list)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relations(self, node: Node) -> list[Edge]:
        return self.edges[node]


