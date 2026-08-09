# 3387. Maximize Amount After Two Days of Conversions

# You are given a string initialCurrency, and you start with 1.0 of initialCurrency.

# You are also given four arrays with currency pairs (strings) and rates (real numbers):

# pairs1[i] = [startCurrencyi, targetCurrencyi] denotes that you can convert from startCurrencyi to targetCurrencyi at a rate of rates1[i] on day 1.
# pairs2[i] = [startCurrencyi, targetCurrencyi] denotes that you can convert from startCurrencyi to targetCurrencyi at a rate of rates2[i] on day 2.
# Also, each targetCurrency can be converted back to its corresponding startCurrency at a rate of 1 / rate.

# You can perform any number of conversions, including zero, using rates1 on day 1, followed by any number of additional conversions, 
# including zero, using rates2 on day 2.
# Return the maximum amount of initialCurrency you can have after performing any number of conversions on both days in order.
# Note: Conversion rates are valid, and there will be no contradictions in the rates for either day. The rates for the days are independent of each other.
# Example 1:
# Input: 
# initialCurrency = "EUR"
# pairs1 = [["EUR","USD"],["USD","JPY"]]
# rates1 = [2.0,3.0]
# pairs2 = [["JPY","USD"],["USD","CHF"],["CHF","EUR"]]
# rates2 = [4.0,5.0,6.0]
# Output: 720.00000
# Explanation:
# To get the maximum amount of EUR, starting with 1.0 EUR:
#     On Day 1:
#         Convert EUR to USD to get 2.0 USD.
#         Convert USD to JPY to get 6.0 JPY.
#     On Day 2:
#         Convert JPY to USD to get 24.0 USD.
#         Convert USD to CHF to get 120.0 CHF.
#         Finally, convert CHF to EUR to get 720.0 EUR.
# Example 2:
# Input: initialCurrency = "NGN", pairs1 = [["NGN","EUR"]], rates1 = [9.0], pairs2 = [["NGN","EUR"]], rates2 = [6.0]
# Output: 1.50000
# Explanation:
# Converting NGN to EUR on day 1 and EUR to NGN using the inverse rate on day 2 gives the maximum amount.
# Example 3:
# Input: initialCurrency = "USD", pairs1 = [["USD","EUR"]], rates1 = [1.0], pairs2 = [["EUR","JPY"]], rates2 = [10.0]
# Output: 1.00000
# Explanation:
# In this example, there is no need to make any conversions on either day.
# Constraints:
#     1 <= initialCurrency.length <= 3
#     initialCurrency consists only of uppercase English letters.
#     1 <= n == pairs1.length <= 10
#     1 <= m == pairs2.length <= 10
#     pairs1[i] == [startCurrencyi, targetCurrencyi]
#     pairs2[i] == [startCurrencyi, targetCurrencyi]
#     1 <= startCurrencyi.length, targetCurrencyi.length <= 3
#     startCurrencyi and targetCurrencyi consist only of uppercase English letters.
#     rates1.length == n
#     rates2.length == m
#     1.0 <= rates1[i], rates2[i] <= 10.0
#     The input is generated such that there are no contradictions or cycles in the conversion graphs for either day.
#     The input is generated such that the output is at most 5 * 1010.

from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rate = [1.0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            parent = self.parent[x]
            self.parent[x] = self.find(parent)
            self.rate[x] *= self.rate[parent]
        return self.parent[x]

    def union(self, x: int, y: int, rate: float) -> None:
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.rate[root_x] = rate * self.rate[y] / self.rate[x]

    def query(self, x: int, y: int) -> float:
        if self.find(x) != self.find(y):
            return -1.0
        return self.rate[x] / self.rate[y]


class Solution:
    def maxAmount(
        self,
        initialCurrency: str,
        pairs1: List[List[str]],
        rates1: List[float],
        pairs2: List[List[str]],
        rates2: List[float],
    ) -> float:
        map_currency_index: dict[str, int] = {}
        num_currencies = 0

        for pair in pairs1 + pairs2:
            for currency in pair:
                if currency not in map_currency_index:
                    map_currency_index[currency] = num_currencies
                    num_currencies += 1

        if initialCurrency not in map_currency_index:
            map_currency_index[initialCurrency] = num_currencies
            num_currencies += 1

        uf1 = UnionFind(num_currencies)
        uf2 = UnionFind(num_currencies)

        for i in range(len(pairs1)):
            uf1.union(
                map_currency_index[pairs1[i][0]],
                map_currency_index[pairs1[i][1]],
                rates1[i],
            )

        for i in range(len(pairs2)):
            uf2.union(
                map_currency_index[pairs2[i][0]],
                map_currency_index[pairs2[i][1]],
                rates2[i],
            )

        initial = map_currency_index[initialCurrency]
        max_amount = 1.0

        for coin in map_currency_index.values():
            day_one = uf1.query(initial, coin)
            day_two = uf2.query(coin, initial)
            if day_one == -1.0 or day_two == -1.0:
                continue
            max_amount = max(max_amount, day_one * day_two)

        return max_amount


# class Solution:
#     def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        
#         def build_graph(pairs, rates):
#             graph = defaultdict(list)
#             for (u, v), rate in zip(pairs, rates):
#                 graph[u].append((v, rate))
#                 graph[v].append((u, 1 / rate))
#             return graph

#         def dfs(graph, cur, amount, visited, res):
#             visited.add(cur)
#             res[cur] = amount
#             for nei, rate in graph[cur]:
#                 if nei not in visited:
#                     dfs(graph, nei, amount * rate, visited, res)

#         graph1 = build_graph(pairs1, rates1)
#         graph2 = build_graph(pairs2, rates2)

#         day1 = {}
#         dfs(graph1, initialCurrency, 1, set(), day1)

#         day2 = {}
#         dfs(graph2, initialCurrency, 1, set(), day2)

#         res = 0
#         for cur, amount in day1.items():
#             if cur in day2:
#                 res = max(res, amount / day2[cur])

#         return res