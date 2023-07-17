def length_of_longest_substring(s: str):
    """
        Steps:
            - initialize set, left pointer an substring count
            - inside right pointer loop, skip all dups and move left pointer
            - add char to set and update substring count w/ max
    """

    l = 0
    res = 0
    char_set = set()

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1
        char_set.add(s[r])
        res = max(res, r-l +1)
    return res


if __name__ == "__main__":
    s = "abcabcbb"
    """
        abc
        abca -> bca
        
        
    """

    length_of_longest_substring(s)
