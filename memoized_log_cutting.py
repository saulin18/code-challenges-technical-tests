
# def cut_log(p, n):
#     if (n == 0):
#         return 0
#     q = -1
#     for i in range(1, n+1):
#         q = max(q, p[i] + cut_log(p, n-i))
#     return q

# https://www.codewars.com/kata/54b058ce56f22dc6fe0011df

def cut_log(p, n):
    dp = [0] * (n+1) # Θ(n) space

    # Some array to store calculated values
    for j in range(1, n+1):
        for i in range(1, j+1):
            dp[j] = max(dp[j], p[i] + dp[j-i]) # Θ(n^2) time
    return dp[n] 
   