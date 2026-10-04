# 1568. Minimum Number of Days to Disconnect Island
# You are given an m x n binary grid grid where 1 represents land and 0 represents water. An island is a
# maximal 4-directionally (horizontal or vertical) connected group of 1's.
# The grid is said to be connected if we have exactly one island, otherwise is said disconnected.
# In one day, we are allowed to change any single land cell (1) into a water cell (0).
# Return the minimum number of days to disconnect the grid.
# Example 1:
# Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
# Output: 2
# Explanation: We need at least 2 days to get a disconnected grid.
# Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
# Example 2:
# Input: grid = [[1,1]]
# Output: 2
# Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m, n <= 30
#     grid[i][j] is either 0 or 1.

from collections import defaultdict, deque


class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        adj_list: dict[tuple[int, int], list[tuple[int, int]]] = defaultdict(list)
        number_of_islands = 0
        visited = [False] * (m * n)
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                adj_list.setdefault((i, j), [])
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        adj_list[(i, j)].append((ni, nj))

                if visited[i * n + j]:
                    continue
                visited[i * n + j] = True
                queue.append((i, j))
                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if (
                            0 <= ni < m
                            and 0 <= nj < n
                            and grid[ni][nj] == 1
                            and not visited[ni * n + nj]
                        ):
                            visited[ni * n + nj] = True
                            queue.append((ni, nj))
                number_of_islands += 1

        if number_of_islands != 1:
            return 0

        if len(adj_list) == 1:
            return 1
        # for (i, j) in adj_list:
        #     grid[i][j] = 0
        #     if not self.is_connected(adj_list, grid):
        #         return 1
        #     grid[i][j] = 1
        
        articulation_points = self.find_articulation_points(adj_list)
        if len(articulation_points) > 0:
            return 1
        return 2

    def is_connected(self, adj_list: dict[tuple[int, int], list[tuple[int, int]]], grid: list[list[int]]) -> bool:
        m = len(grid)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        n = len(grid[0])
        number_of_islands = 0
        visited = [False] * (m * n)
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] != 1:
                    continue
                if visited[i * n + j]:
                    continue
                visited[i * n + j] = True
                queue.append((i, j))
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        queue.append((ni, nj))
                        visited[ni * n + nj] = True
                     
                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in directions:
                        ni, nj = ci + di, cj + dj
                        if (
                            0 <= ni < m
                            and 0 <= nj < n
                            and grid[ni][nj] == 1
                            and not visited[ni * n + nj]
                        ):
                            visited[ni * n + nj] = True
                            queue.append((ni, nj))
                number_of_islands += 1
        
        return number_of_islands == 1

    def find_articulation_points(
        self, adj_list: dict[tuple[int, int], list[tuple[int, int]]]
    ) -> list[tuple[int, int]]:
        disc: dict[tuple[int, int], int] = {}
        low: dict[tuple[int, int], int] = {}
        visited: set[tuple[int, int]] = set()
        articulation_points: set[tuple[int, int]] = set()
        timer = [0]

        def tarjan(node: tuple[int, int], parent: tuple[int, int] | None) -> None:
            visited.add(node)
            disc[node] = low[node] = timer[0]
            timer[0] += 1
            children = 0

            for neighbour in adj_list[node]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    low[node] = min(low[node], disc[neighbour])
                    continue
                children += 1
                tarjan(neighbour, node)
                low[node] = min(low[node], low[neighbour])
                if parent is not None and low[neighbour] >= disc[node]:
                    articulation_points.add(node)

            if parent is None and children > 1:
                articulation_points.add(node)

        for node in adj_list:
            if node not in visited:
                tarjan(node, None)

        return list(articulation_points)
