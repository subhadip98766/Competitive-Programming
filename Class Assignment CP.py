# ==============================
# Problem 1: Longest Palindromic Substring
# ==============================
def longestPalindrome(s):
    longest = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            part = s[i:j+1]
            if part == part[::-1] and len(part) > len(longest):
                longest = part
    return longest


# ==============================
# Problem 2: Regular Expression Matching ('.' and '*')
# ==============================
def isMatch(s, p):
    if not p:
        return not s
    first_match = bool(s) and (p[0] in {s[0], '.'})
    if len(p) >= 2 and p[1] == '*':
        return (isMatch(s, p[2:]) or
                (first_match and isMatch(s[1:], p)))
    else:
        return first_match and isMatch(s[1:], p[1:])


# ==============================
# Problem 3: Generate Parentheses
# ==============================
def generateParenthesis(n):
    result = []
    def backtrack(curr, openN, closeN):
        if len(curr) == 2 * n:
            result.append(curr)
            return
        if openN < n:
            backtrack(curr + "(", openN + 1, closeN)
        if closeN < openN:
            backtrack(curr + ")", openN, closeN + 1)
    backtrack("", 0, 0)
    return result


# ==============================
# Problem 4: Climbing Stairs
# ==============================
def climbStairs(n):
    if n == 1:
        return 1
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


# ==============================
# Problem 5: Best Time to Buy and Sell Stock
# ==============================
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit


# ==============================
# Run Test Cases
# ==============================
print("Problem 1: Longest Palindrome")
print("Input: babad -> Output:", longestPalindrome("babad"))
print("Input: cbbd  -> Output:", longestPalindrome("cbbd"))
print()

print("Problem 2: Regex Matching")
print('Input: ("aa", "a")   -> Output:', isMatch("aa", "a"))
print('Input: ("aa", "a*")  -> Output:', isMatch("aa", "a*"))
print('Input: ("ab", ".")  -> Output:', isMatch("ab", "."))
print()

print("Problem 3: Generate Parentheses")
print("Input: 3 -> Output:", generateParenthesis(3))
print("Input: 1 -> Output:", generateParenthesis(1))
print()

print("Problem 4: Climbing Stairs")
print("Input: 2 -> Output:", climbStairs(2))
print("Input: 3 -> Output:", climbStairs(3))
print()

print("Problem 5: Max Profit")
print("Input: [7,1,5,3,6,4] -> Output:", maxProfit([7,1,5,3,6,4]))
print("Input: [7,6,4,3,1]   -> Output:", maxProfit([7,6,4,3,1]))
