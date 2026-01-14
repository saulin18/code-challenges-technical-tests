
#605. Can Place Flowers
#Easy
#Topics
#premium lock icon
#Companies
#You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
#Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
#
#Example 1:
#
#Input: flowerbed = [1,0,0,0,1], n = 1
#Output: true
#Example 2:
#
#Input: flowerbed = [1,0,0,0,1], n = 2
#Output: false

def canPlaceFlowers(self, flowerbed, n):
    
        for index in range(len(flowerbed)):
            if n == 0:
                return True
            
            if flowerbed[index] == 0 and (flowerbed[index - 1]  == 0 and index != 0 ) and (index == len(flowerbed) - 1 or flowerbed[index + 1] == 0):
                flowerbed[index] = 1
                n -= 1
        
        
        return n <= 0 

