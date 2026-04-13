# 1626. Best Team With No Conflicts
# You are the manager of a basketball team.
# For the upcoming tournament,
# you want to choose the team with the highest overall score.
# The score of the team is the sum of scores of all the players in the team.
# However, the basketball team is not
# allowed to have conflicts. A conflict exists if a younger player
# has a strictly higher score than an older player. A conflict does
# not occur between players of the same age.
# Given two lists, scores and ages,
# where each scores[i] and ages[i]
# represents the score and age of the
# ith player, respectively, return the
# highest overall score of all possible basketball teams.
# Example 1:
# Input: scores = [1,3,5,10,15], ages = [1,2,3,4,5]
# Output: 34
# Explanation: You can choose all the players.
# Example 2:
# Input: scores = [4,5,6,5], ages = [2,1,2,1]
# Output: 16
# Explanation: It is best to choose the last 3 players. Notice that you are allowed to choose multiple people of the same age.
# Example 3:
# Input: scores = [1,2,3,5], ages = [8,9,10,1]
# Output: 6
# Explanation: It is best to choose the first 3 players.
# Constraints:
# 1 <= scores.length, ages.length <= 1000
# scores.length == ages.length
# 1 <= scores[i] <= 106
# 1 <= ages[i] <= 1000


from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:

        sorted_players = sorted(zip(scores, ages), key=lambda x: (x[1], x[0]))
        n = len(sorted_players)

        def recursive(index: int, minimum_score: int, memo: dict) -> int:
            if index >= n:
                return 0

            current_score, age = sorted_players[index]

            if (index, minimum_score) in memo:
                return memo[(index, minimum_score)]

            if current_score < minimum_score:
                memo[(index, minimum_score)] = recursive(index + 1, minimum_score)
                return memo[(index, minimum_score)]

            without_player = recursive(index + 1, minimum_score)

            with_player = recursive(index + 1, current_score) + current_score

            memo[(index, minimum_score)] = max(without_player, with_player)
            return memo[(index, minimum_score)]

        return recursive(0, float("-inf"), {})
