from collections import deque

n,k,q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))
res = deque(a)
res.rotate(k)
a = list(res)
for x in range(q):
    x = int(input())
    print(a[x])
