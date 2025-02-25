def characterReplacement(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    retval = 0
    charset = set(s)
    for c in charset:
        l = maxchar = 0
        for r in range(len(s)):
            if s[r] == c:
                maxchar += 1
            while (r - l + 1) - maxchar > k:
                if s[l] == c:
                    maxchar -= 1
                l += 1
            retval = max(retval, r - l + 1)
    return retval
