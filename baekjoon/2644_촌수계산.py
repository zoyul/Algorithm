n = int(input())
a, b = map(int, input().split())
k = int(input())
arr = [[] for _ in range(n+1)]
for i in range(k):
    q, p = map(int, input().split())
    arr[q].append(p)
    arr[p].append(q)

# 공백 큐 생성, 시작점 넣기, 방문표시
q = []
q.append(b)
visited = [0] * (n+1)
visited[b] = 1

# q가 비워질 때 까지
while q:
    # 현재 위치한 사람과 1촌인 사람 q에 넣기
    now = q.pop(0)
    for i in arr[now]:
        if visited[i] == 0:
            q.append(i)
            visited[i] = visited[now] + 1

if visited[a] == 0:
    print(-1)
else:
    print(abs(visited[a]-visited[b]))