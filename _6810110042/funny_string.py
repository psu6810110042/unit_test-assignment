def funnyString(s):
    diffs = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]

    if diffs == diffs[::-1]:
        return "Funny"
    else:
        return "Not Funny"
