s = 'AAAA'
count_A = 0
count_L = 0
res = True
for i in range(len(s)):
    if s[i] != 'L':
        count_L = 0
        if s[i] == 'A':
            count_A += 1
            if count_A >= 2:
                res = False
                break
    else:
        count_L += 1
        if count_L >= 3:
            res = False
            break


print(res)
