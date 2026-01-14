#1079. Letter Tile Possibilities
#Medium
#Topics
#premium lock icon
#Companies
#Hint
#You have n  tiles, where each tile has one letter tiles[i] printed on it.
#
#Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
#
# 
#
#Example 1:
#
#Input: tiles = "AAB"
#Output: 8
#Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
#Example 2:
#
#Input: tiles = "AAABBC"
#Output: 188
#Example 3:
#
#Input: tiles = "V"
#Output: 1
# 
#
#Constraints:
#
#1 <= tiles.length <= 7
#tiles consists of uppercase English letters.

def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        
        result = set()
        used = [False] * len(tiles)
        
        def backtrack(actual: str):
            if len(actual) > 0:
                result.append(actual)
            

            for end in range(tiles):
                if not used[end]:
                    used[end] = True
                    actual += tiles[end]
                    backtrack(end + 1, actual)
                    actual = actual[:-1]
                    used[end] = False
                    
        backtrack(0, "")
        
        return len(result)            
            
        