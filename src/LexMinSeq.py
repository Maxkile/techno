inp = input().split(' ')
k = int(inp.pop())
n = int(inp.pop())
res = list()
for i in range(0,n-k+2,1):
    if i%2 == 0:
        res.append(1)
    else:
        res.append(2)
next = 3
for j in range(n-k+2,n,1):
    res.append(next)
    next+=1
for j in range(0,len(res)):
    print(res[j],end=' ')