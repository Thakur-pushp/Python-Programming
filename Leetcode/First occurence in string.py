haystack = "usadsautsad"
needle = "sad"
lenneedle = len(needle)
lenhaystack = len(haystack)
if needle not in haystack:
    print(-1)
else:
    i = 0
    while i<lenhaystack:
        if haystack[i:lenneedle] != needle:
            i += 1
            lenneedle += 1
        elif haystack[i:lenneedle] == needle:
            print(i)
            break