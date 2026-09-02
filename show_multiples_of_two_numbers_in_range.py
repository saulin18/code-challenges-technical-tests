
# Show multiples of 2 numbers within a range
# Given 3 positive parameters a, b, limit, return all positive numbers that are a 
# multiple of both a and b up to and including limit.
# Examples
# 1, 5, 15 --> [5, 10, 15]
# 3, 5, 15 --> [15]
# 3, 5, 40 --> [15, 30]
# 2, 4, 40 --> [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]

def multiples(a: int, b: int, limit: int) -> list[int]:
    return [ i for i in range(min(a, b), limit + 1) if i % a == 0 and i % b == 0]