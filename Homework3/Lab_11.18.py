# Michael Donald
# 1896510

x = input().split()
result = []
for v in x:
    v = int(v)
    if v >= 0:
        result.append(v)
result.sort()
for v in result:
    print(v, end=' ')
