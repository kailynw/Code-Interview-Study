
def isAnagram(s, t):
        # In case of different length of thpse two strings...
        if len(s) != len(t):
            return False

        set_s = set(s)
        for letter in set_s:
            # Compare s.count(l) and t.count(l) for every index i from 0 to 26...
            # If they are different, return false...

            s_count = s.count(letter)
            t_count = t.count(letter)
            if s.count(letter) != t.count(letter):
                return False
        return True     # Otherwise, return true...

if __name__ == "__main__":
    s = "anagram"
    t = "gramana"

    result = isAnagram(s, t)
    print(result)