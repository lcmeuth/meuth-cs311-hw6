"""
Homework 6: The Prerequisite Planner -- starter.

Complete has_cycle and topological_sort below. See
Homework 6 The Prerequisite Planner.md, Part B, for the full requirements.
"""

from typing import Dict, List, Optional


def has_cycle(graph: Dict[str, List[str]]) -> bool:
    """
    Recursive DFS. Track both a permanent "visited" set and a
    temporary "on the current recursion path" set to detect back
    edges (Part A, Question 4). Must work across disconnected
    components.
    """
    visited=set()
    onPath=set()

    def dfs(node: str) -> bool:
        if node in onPath:
            return True
        if node in visited:
            return False

        visited.add(node)
        onPath.add(node)

        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True

        onPath.remove(node)
        return False

    nodes = set(graph)
    for neighbors in graph.values():
        nodes.update(neighbors)

    return any(dfs(node) for node in nodes if node not in visited)


def topological_sort(graph: Dict[str, List[str]]) -> Optional[List[str]]:
    """
    Return a valid topological order via DFS finish-time ordering
    (Part A, Questions 2-3), or None if the graph contains a cycle.
    """
    visited = set()
    onPath = set()
    order = []

    def dfs(node: str) -> bool:
        if node in onPath:
            return False
        if node in visited:
            return True

        visited.add(node)
        onPath.add(node)

        for neighbor in graph.get(node, []):
            if not dfs(neighbor):
                return False

        onPath.remove(node)
        order.append(node)
        return True

    nodes = set(graph)
    for neighbors in graph.values():
        nodes.update(neighbors)

    for node in nodes:
        if node not in visited and not dfs(node):
            return None

    order.reverse()
    return order