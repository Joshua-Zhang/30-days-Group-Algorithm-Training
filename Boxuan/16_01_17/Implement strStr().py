def strStr(self, haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    n , m = len(haystack), len(needle)
    for i in range(n + 1):
        for j in range(m + 1):
            if j == m:
                return i
            if i + j == n:
                return -1
            if haystack[i + j] != needle[j]:
                break