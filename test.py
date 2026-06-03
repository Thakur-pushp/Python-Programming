pattern = "abba"
s = "dog cat cat dog"

# Store 'S' in list
lt = s.split()

# Dictionary for mapping
dic = {}

# Result by default True
res = True


# Loop in pattern
for i in range(len(pattern)):
    # Checking if a value already exist in dictionary
    if lt[i] in dic.values():
        res = False
    else:
        dic[pattern[i]] = lt[i]
    
strs = [].append (dic[pattern[j]] for j in range(len(pattern)))

if lt == strs:
    res = True 
else:
    res = False

print(res)
    