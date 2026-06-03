candyType = [6,6,6,6]
total_candy = len(candyType)
kind = len(set(candyType))
eat = total_candy//2
if kind == eat or kind < eat:
    print(kind)
else:
    print(eat)
