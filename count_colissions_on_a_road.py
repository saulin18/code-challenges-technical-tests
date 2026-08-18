# 2211. Count Collisions on a Road
# There are n cars on an infinitely long road. The cars are numbered from 0 to n - 1 from left to right and each car is present at a unique point.

# You are given a 0-indexed string directions of length n. directions[i] can be either 'L', 'R', or 'S' denoting whether
# the ith car is moving towards the left, towards the right, or staying at its current point respectively. Each moving car has the same speed.
# The number of collisions can be calculated as follows:
#     When two cars moving in opposite directions collide with each other, the number of collisions increases by 2.
#     When a moving car collides with a stationary car, the number of collisions increases by 1.
# After a collision, the cars involved can no longer move and will stay at the point where they collided.
# Other than that, cars cannot change their state or direction of motion.
# Return the total number of collisions that will happen on the road.
# Example 1
# Input: directions = "RLRSLL"
# Output: 5
# Explanation:
# The collisions that will happen on the road are:
# - Cars 0 and 1 will collide with each other. Since they are moving in opposite directions, the number of collisions becomes 0 + 2 = 2.
# - Cars 2 and 3 will collide with each other. Since car 3 is stationary, the number of collisions becomes 2 + 1 = 3.
# - Cars 3 and 4 will collide with each other. Since car 3 is stationary, the number of collisions becomes 3 + 1 = 4.
# - Cars 4 and 5 will collide with each other. After car 4 collides with car 3, it will stay at the point of collision
# and get hit by car 5. The number of collisions becomes 4 + 1 = 5.
# Thus, the total number of collisions that will happen on the road is 5.
# Example 2:
# Input: directions = "LLRR"
# Output: 0
# Explanation:
# No cars will collide with each other. Thus, the total number of collisions that will happen on the road is 0.


# Constraints:

#     1 <= directions.length <= 105
#     directions[i] is either 'L', 'R', or 'S'.


from ast import Starred
class Solution:
    def countCollisions(self, directions: str) -> int:
        # stack = []
        # collisions = 0
        # for direction in directions:
        #     collision = False

        #     count_of_rs = 0
        #     while stack and stack[-1] == 'R' and direction == 'L':
        #         collision = True
        #         stack.pop()
        #         count_of_rs += 1
        #     collisions += count_of_rs + 1 if count_of_rs > 0 else 0
        #     while stack and stack[-1] == 'R' and direction == 'S':
        #         collision = True
        #         stack.pop()
        #         collisions += 1

        #     while stack and stack[-1] == 'S' and direction == 'L' and count_of_rs == 0:
        #         collision = True
        #         stack.pop()
        #         collisions += 1
        #         break
        #     if not collision:
        #         stack.append(direction)
        #     else:
        #         stack.append('S')
        # return collisions
        n = len(directions)
        start = 0
        end = 0
       
        while start < n and directions[start] == "L":
            start += 1
        while end >= 0 and directions[end] == "R":
            end -= 1

        return sum(1 for i in range(start, end + 1) if directions[i] != "S")


# class Solution:
#     def countCollisions(self, directions: str) -> int:
#         dirs = directions.lstrip("L").rstrip("R")
#         return len(dirs) - dirs.count("S")
#         # collisions = 0
#         # direction = list(directions)
#         # for (idx, car) in enumerate(direction):
#         #     if car == "L":
#         #         if idx > 0 and direction[idx-1] != "L":
#         #             collisions += 1
#         #             direction[idx] = "S"
#         #     if car == "R":
#         #         if idx != len(direction) -1 and direction[idx + 1] != "R":
#         #             collisions += 1
#         #             direction[idx] = "S"

                
#         # return collisions

# # testing

# # directions = "RLRSLL"
# # collisions = 0
# # 0,R 1
# # 1,L 2
# # 2,R 3
# # 3,S 3
# # 4,L 4
# # 5,L 5
