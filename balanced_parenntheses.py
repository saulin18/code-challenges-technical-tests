# Write a function which makes a list of strings representing all of the ways you can balance n pairs of parentheses
#
# Examples
# balanced_parens(0) => [""]
# balanced_parens(1) => ["()"]
# balanced_parens(2) => ["()()","(())"]
# balanced_parens(3) => ["()()()","(())()","()(())","(()())"


def balanced_parens(n):
    if n == 0:
        return [""]

    res = []

    def backtrack(to_open, to_close, curr):
        if to_open > 0:
            backtrack(to_open - 1, to_close + 1, curr + "(")

        if to_close > 0:
            backtrack(to_open, to_close - 1, curr + ")")

        if to_open == 0 and to_close == 0:
            res.append(curr)

    backtrack(n, 0, "")

    return res


balanced_parens(3)
