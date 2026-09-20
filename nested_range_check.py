
# Nested Ranges Check.
# Time limit: 2.0s
# Memory limit: 512M
# Author:
# FrankHG

# Dados n rangos, su tarea consiste en determinar para cada rango si contiene algún otro 
# rango y si algún otro rango lo contiene. El rango [a,b] contiene al rango [c,d] si a≤c y d≤b.

# Entrada
# La primera línea de entrada tiene un número entero n: el número de rangos. Después, hay 
# n líneas que describen los rangos. Cada línea tiene dos enteros
# x e y: el rango es [x,y]. Puede suponer que ningún rango aparece más de una vez en la entrada.
# Salida
# Primero imprima una línea que describa para cada rango (en el orden de entrada) si contiene algún 
# otro rango (1) o no (0). A continuación, imprima una línea que describa para
# cada rango (en el orden de entrada) si algún otro rango lo contiene (1) o no (0).
# Restricciones

#     1≤n≤2⋅105
#     1≤x<y≤109

# Ejemplo de Entrada

# 1 6
# 2 4
# 4 8
# 3 6

# Ejemplo de Salida

# 1 0 0 0
# 0 1 0 1

def nested_range_check(ranges):
   
    sorted_ranges = sorted(ranges, key=lambda t: (t[0], -t[1]))
    n = len(ranges)
    contained = [0] * n 
    contains = [0] * n  
    maximum_end = -1
    minimum_end = float("inf")

    for x, y, idx in sorted_ranges:
        if y <= maximum_end:
            contained[idx] = 1
        maximum_end = max(maximum_end, y)

    for x, y, idx in reversed(sorted_ranges):
        if minimum_end <= y:
            contains[idx] = 1
        minimum_end = min(minimum_end, y)

    return contains, contained

if __name__ == "__main__":
    n = int(input())
    ranges = []
    for i in range(n):
        x, y = map(int, input().split())
        ranges.append((x, y, i))

    contains, contained = nested_range_check(ranges)
    print(" ".join(map(str, contains)))
    print(" ".join(map(str, contained)))