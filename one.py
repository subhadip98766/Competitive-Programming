def longestPalindrome(s: str) -> str:
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    res = ""
    for i in range(len(s)):
        res = max(res, expand(i, i), expand(i, i+1), key=len)
    return res


# Example test
print(longestPalindrome("babad"))  # "bab" or "aba"
print(longestPalindrome("cbbd"))   # "bb"
