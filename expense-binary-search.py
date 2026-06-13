# Gasto Mensual.
# El Granjero Juan es un mago asombroso para la contabilidad y se ha dado cuenta
# que podría quedarse sin dinero para manejar la granja.
# El ya ha calculado y registrado la cantidad exacta de dinero que él
# siempre necesitará cada día en los siguientes N
# días.

# GJ quiere crear un presupuesto para un conjunto secuencial de exactamente M
# períodos fiscales llamados "fajomeses".
# Cada uno de estos fajomeses contiene un conjunto de 1 ó más días consecutivos.
# Cada día está contenido en exactamente un fajomes.

# El objetivo de GJ es organizar los fajomeses de tal manera de minimizar
# los gastos del fajomes con el mayor gasto y por lo tanto determinar su límite de gasto mensual.

# Entrada
# Línea 1: Dos enteros separados por un espacio, N y M:
#  y
# Líneas 2..N+1: La línea
#  contiene el número de dólares que el Granjero Juan gasta en el día i-ésimo.
# Salida
# En una sola menor límite mensual posible que el Granjero Juan debe tener para sobrevivir.

# Restricciones
# Ejemplo de Entrada
# Copiar
# 7 5
# 100
# 400
# 300
# 100
# 500
# 101
# 400
# Detalles de la Entrada: Hay 7 días para distribuir a través de 5 fajomeses. El gasta
#  y
#  en días consecutivos.
# Ejemplo de Salida
# 500
# Detalles de la Salida: Si el Granjero Juan programa los meses de tal manera que los
# dos primeros días son un mes, el tercero y el cuarto son un mes,
# y los últimos tres sean sus propios meses, él gasta a lo más $500 en cada mes.
# Cualquier otro método de programación da un limite de mínimo mensual más grande.

#
# 100 400   300 100   500   101   400   Gasto Diario
# ---1---   ---2---   -3-   -4-   -5-   Número de Mes
#   500       400     500   101   400   Gasto Mensual
# USACO MAR07 Silver Problem 'expense'


def solve(m: int, expenses_per_month: list[int]) -> int:

    left = 0
    right = max(expenses_per_month)
    
    def can(average_expense: int) -> bool:
        current_expense = 0
        months = 0
        for expense in expenses_per_month:
            current_expense += expense
            if current_expense > average_expense:
                current_expense = 0
                months += 1
        return months + 1 <= m

    while left <= right:
        mid = left + (right - left) // 2

        if can(mid):
            right = mid - 1
        else:
            left = mid + 1

    return left


n, m = int(input().strip().split())
expenses_per_month = []
while n:
    expenses_per_month.append(input().strip())
    n -= 1

# Binary search
res = solve(m, expenses_per_month)
print(res)