# 207. Course Schedule
# There are a total of numCourses courses you have to take,
# labeled from 0 to numCourses - 1. You are given an array
# prerequisites where prerequisites[i] = [ai, bi] indicates
# that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0
# you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.

# Example 1:

# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:

# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course
# 0 you should also have finished course 1. So it is impossible.
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
from typing import List, Dict
from enum import Enum
from collections import defaultdict


class State(Enum):
    VISITED = 2
    NOT_VISITED = 0
    VISITING = 1


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        node_states = [State.NOT_VISITED] * numCourses

        def build_graph(prerequisites: List[List[int]]) -> Dict[int, List[int]]:
            graph = defaultdict(list)
            for course, prerequisite in prerequisites:
                graph[course].append(prerequisite)
            return graph

        adj_list = build_graph(prerequisites)

        def dfs(node: int, node_states: List[State]) -> bool:
            if node_states[node] == State.VISITED:
                return True
            if node_states[node] == State.VISITING:
                return False

            node_states[node] = State.VISITING

            for neighbor in adj_list[node]:
                if not dfs(neighbor, node_states):
                    return False

            node_states[node] = State.VISITED
            return True

        for course in range(numCourses):
            if node_states[course] == State.NOT_VISITED:
                if not dfs(course, node_states):
                    return False
        return True
    
        
    # class Solution:
    #     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

    #         graph = {i:[] for i in range(numCourses)}
    #         for a, b in prerequisites:
    #             graph[b].append(a)
            
    #         # Cycle detection
    #         path = set()
    #         visited = set()

    #         def dfs(node):

    #             if node in path:
    #                 return False
    #             if node in visited:
    #                 return True

    #             path.add(node)

    #             for neighbour in graph[node]:
    #                 if not dfs(neighbour):
    #                     return False
    #             path.remove(node)
    #             visited.add(node)
    #             return True

    #         for node in range(numCourses):
    #             if not dfs(node):
    #                 return False

    #         return True


# from collections import deque, defaultdict

# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
#         deps_map = defaultdict(list)
#         in_degree = [0] * numCourses 

#         for a,b in prerequisites:
#             deps_map[b].append(a)
#             in_degree[a] += 1

        
#         q = deque([i for i in range(numCourses) if in_degree[i] == 0])

#         curr_count = 0
#         while q:
#             curr = q.popleft()
#             curr_count += 1

#             for t in deps_map[curr]:
#                 in_degree[t] -= 1

#                 if in_degree[t] == 0:
#                     q.append(t)
                
#         return curr_count == numCourses