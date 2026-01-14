#
# Range Extraction
# 317761891% of 5,83619,521 of 63,049jhoffner
#
# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.
#
# Example:
#
# solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]);
# // returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
# Courtesy of rosettacode.org


def solution(args):
    # Args is a number array
    # I think that we can follow a Two pointers approach

    # 1. Pointer a, pointer b, both starting at 0, if a and b are consecutive, move b forward
    # If not calculate the distance between a and b and do the transformation with that segment, a-b and move a to b

    result = []

    def format_range(r: int, a: int, b: int, args: list[int]):
        if r >= 3:
            return f"{args[a]}-{args[b - 1]}"
        elif r == 2:
            return [args[a], args[a + 1]]
        else:
            return args[a]

    a = 0
    for b in range(1, len(args)):
        if not args[b - 1] + 1 == args[b]:
            if b - a >= 3:
                result.append(format_range(b - a, a, b, args))
            elif b - a == 2:
                result.extend(format_range(b - a, a, b, args))
            else:
                result.append(format_range(b - a, a, b, args))

            a = b

    len_of_missing_segment = len(args) - a
    if len_of_missing_segment >= 3:
        result.append(format_range(len_of_missing_segment, a, len(args), args))
    else:
        for i in range(a, len(args)):
            result.append(format_range(1, i, i + 1, args))

    print(result)

    return ",".join(map(str, result))


import decimal


def round_by_2_decimal_places(n: decimal.Decimal) -> decimal.Decimal:
    return decimal.Decimal(n).quantize(
        decimal.Decimal(""),
        rounding=decimal.ROUND_HALF_UP,
    )
