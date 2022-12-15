n = int(input())
arr = map(int, input().split())

alist = []
for i in arr:
    alist.append(i)

for i in range(len(alist)):
    a = max(alist)
    alist.remove(a)
    ans = max(alist)
    if ans != a:
        break

print(ans)