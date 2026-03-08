str = "aaaabbbcca"


def solve(str):
    res = []
    count_of_actual_char = 0
    for i, char in enumerate(str):
        if i > 0:
            if str[i] != str[i - 1]:
                res.append((str[i - 1], count_of_actual_char))
                count_of_actual_char = 0
        if i == len(str) - 1:
            res.append((char, count_of_actual_char + 1))
        count_of_actual_char += 1
    return res


print(solve(str))
print(solve("a"))