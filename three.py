def generateParenthesis(n: int):
    res = []

    def backtrack(curr, open_count, close_count):
        if len(curr) == 2 * n:
            res.append(curr)
            return
        if open_count < n:
            backtrack(curr + "(", open_count + 1, close_count)
        if close_count < open_count:
            backtrack(curr + ")", open_count, close_count + 1)

    backtrack("", 0, 0)
    return res


# Example test
print(generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(generateParenthesis(1))  # ["()"]
