# Given a string, find the length of the longest substring without repeating
# characters.


def longestSubstring(s):
    used = {}
    maxlen = start = 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            maxlen = max(maxlen, i - start + 1)      
        used[c] = i

    substr = s[start : start + maxlen]
    print(substr,"has length", len(substr))

s = input()
longestSubstring(s)
