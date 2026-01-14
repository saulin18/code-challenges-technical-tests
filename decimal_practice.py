import decimal


def decimal_from_a_float_and_from_a_string(num: float, string: str):
    return (decimal.Decimal(num), decimal.Decimal(string))


# 2. Rounding Up/Down Configuration
#
# Write a Python program to configure rounding to round up and round down a given decimal value. Use decimal.Decimal

def round_to_10_cents(x):
    remainder = x.remainder_near(decimal.Decimal("0.10"))
    if abs(remainder) == decimal.Decimal("0.05"):
        return x
    else:
        return x - remainder


def rounding_down_or_up_to_given_decimal_values(mode: str, decimal_values: int, numb: float):

    decimal_num = decimal.Decimal(numb)
    
    exp = decimal.Decimal(10) ** -decimal_values
    
    rounding_mode = decimal.ROUND_UP if mode == "up" else decimal.ROUND_DOWN
    
    return decimal_num.quantize(exp, rounding=rounding_mode)

print(rounding_down_or_up_to_given_decimal_values("down", 4, 10.165665))