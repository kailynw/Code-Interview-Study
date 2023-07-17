def word_break(s, words):
    d = [False] * len(s)
    for i in range(len(s)):
        for w in words:
            sub_s = s[i-len(w)+1:i+1]
            cond_1 = d[i-len(w)]
            cond_2 = i-len(w) == -1 #
            if w == sub_s and (cond_1 or cond_2):
                d[i] = True
    return d[-1]

if __name__ == "__main__":
    s = "leetcode"
    words = ["leet", "code"]
    print(word_break(s, words))