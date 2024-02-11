def alternatingCharacters(s):
    deletion = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            deletion = deletion + 1
    return deletion