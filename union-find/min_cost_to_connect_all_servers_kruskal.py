
# # Problem: Minimum Cost to Connect All Servers

# You're a network engineer at a data center. There are n servers positioned on a 2D grid. Each server
#  is given as `points[i] = [xi, yi]`.
# You want to connect all the servers so that there is exactly one path between any two
#  servers (i.e., the network is fully connected). The cost to connect two servers is 
# the Manhattan distance between them:
# ```
# cost(i, j) = |xi - xj| + |yi - yj|
# ```
# Return the minimum total cost to connect all n servers such that every server is reachable 
# from every other server.
# ## Example 1:
# ```
# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# ```
# ## Example 2:
# ```
# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
# ```
# ## Solution
# In order to solve this problem here I would use below data structures and approach

# The problem here is basically a graph problem where points are the nodes in the graph and edges 
# between them denote the cost to connect them
# This problem basically boils down to connecting all points together to form one path with 
# minimum cost which takes to using a data structure called union find.
# I would use this sort of data structure because it efficiently gives me the capability 
# to union two points and see if two points belong to the same set. Ultimately since we want to join
# all points together, I would just check if the no of components in the union find 
# data structure is 1.

# Since we want to minimize the total cost in connecting all the points together, I would use a 
# greedy approach by sorting the points by cost to connect them
# ### Data structure
# - Union find: This would be used to store connected components together
#  and to determine if two points belong to the same component
# ### Approach

# - Loop over the points list
# - For each point x, loop over all other points and for each point y
#     - Compute the manhattan distance between them
#     - Store the index of the x, y and the distance between them in a result list
# - Sort the result list by cost so that we take minimum cost ones before
# - Initialize the union find data structure for n points where n = len(points)
# - Initialize total_cost = 0
# - Loop over result list, for each item - (pointx, pointy, cost)
#     - If no of connected components = 1, break from loop
#     - Else, try union of pointx and pointy, if union returns true, sum up total_cost with cost
# - At the end return total_cost

# ### Time complexity

# - Loop to compute cost for each point takes - O(N^2)
# - Sorting the result list takes - O(N^2logN)
# - Looping over each item in result list and doing operations in union find 
# takes around O(N^2AlphaN) time, where union and find operations in union find data 
# structure takes alpha(n) time where alpha is inverse ackermann function.

# ### Space complexity

# - O(N^2), where N = no of points

class UnionFind:
    def __init__(self, n: int):
        self.n = n
        self.rank: list[int] = [0] * (n)
        self.parent: list[int] = [i for i in range(n)]

    def find(self, x) -> int:
        if x == self.parent[x]:
            return x
        
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        parx = self.find(x)
        pary = self.find(y)

        if parx == pary:
            return False

        if self.rank[parx] < self.rank[pary]:
            self.parent[parx] = pary

        elif self.rank[pary] < self.rank[parx]:
            self.parent[pary] = parx        
        else:
            self.parent[pary] = parx
            self.rank[parx] += 1

        self.n -= 1
        return True

class Network:
    def min_cost_to_connect(self, points: list[list[int]]) -> int:
        n = len(points)

        if n == 1:
            return 0

        result: list[list[int]] = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                result.append([i, j, dist])

        result.sort(key=lambda point: point[2])

        uf = UnionFind(n)
        total_cost = 0

        for point in result:
            if uf.n == 1:
                break
            if uf.union(point[0], point[1]):
                total_cost += point[2]

        return total_cost