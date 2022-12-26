n, k = map(int, input().split())
visited = [0] * 100001

di = [-1, 1, 2]

q = []
q.append(n)
visited[n] = 1

while q:
    now = q.pop(0)

    for a in range(3):
        next = now + di[a]

        if a == 2:
            next = now * 2

        if next < 0 or next >= len(visited):
            continue
        if visited[next] != 0:
            continue

        visited[next] = visited[now] + 1
        q.append(next)

print(visited[k]-1)