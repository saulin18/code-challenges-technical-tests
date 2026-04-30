def lcs_recurrence(s1, s2, m, n): 
  if m == -1 or n == -1:
    return 0
  
  if s1[m] == s2[n]:
    return 1 + lcs_recurrence(s1, s2, m-1, n-1)
  
  return max(lcs_recurrence(s1,s2, m-1,n), lcs_recurrence(s1,s2, m,n-1))

def lcs_dp(X, Y):
  m = len(X)
  n = len(Y)
  
  # crear tabla de programación dinámica
  L = [[0] * (n + 1) for _ in range(m + 1)]
    
  # completar tabla 
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if X[i - 1] == Y[j - 1]:
        L[i][j] = L[i - 1][j - 1] + 1
      else:
        L[i][j] = max(L[i - 1][j], L[i][j - 1])
  
  # reconstruir la LCS
  lcs = ""
  i, j = m, n
  while i > 0 and j > 0:
    if X[i - 1] == Y[j - 1]:
      lcs = X[i - 1] + lcs
      i -= 1
      j -= 1
    elif L[i - 1][j] > L[i][j - 1]:
      i -= 1
    else:
      j -= 1
    
  return L, L[m][n], lcs

if __name__ == "__main__":
  s1 = "ABCD\nXD"
  s2 = "ACBD\n\nXD"
  #print(lcs(s1,s2, len(s1) - 1, len(s2) - 1))
  print(lcs_dp(s1,s2))