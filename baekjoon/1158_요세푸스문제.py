n, k = map(int, input().split())
q = []
for i in range(1, n+1):
    q.append(i)

now = 0
result = []
while q:
    now = (now + (k-1)) % len(q)
    result += [q.pop(now)]

print('<' + ', '.join(map(str, result)) + '>')