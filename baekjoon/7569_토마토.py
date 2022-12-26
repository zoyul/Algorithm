import sys
from collections import deque               # 이거 안쓰면 시간초과나옴

m, n, h = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n*h)]

q = deque()

di = [1, -1, 0, 0, n, -n]           # 층을 옮겨다니는 걸 n으로 움직임
dj = [0, 0, 1, -1, 0, 0]

for i in range(n*h)[::-1]:
    for j in range(m):
        if arr[i][j] == 1:      # 익은 토마토라면 시작점으로
            q.append([i, j])

ans = -1
while q:
    now = q.popleft()
    now_i = now[0]
    now_j = now[1]
    ans = arr[now_i][now_j]

    for k in range(6):
        if k == 0:
            if (now_i + di[k]) % n == 0:            # 아래로 내려갈 때 만약 층을 움직이게 된다면 무시
                continue
        if k == 1:
            if (now_i + di[k] + 1) % n == 0:
                continue
        next_i = now_i + di[k]
        next_j = now_j + dj[k]

        if next_i < 0 or next_i >= n*h or next_j < 0 or next_j >= m:      # 범위 넘어가면 무시 안익은 토마토아니면 무시
            continue
        if arr[next_i][next_j] != 0:
            continue

        arr[next_i][next_j] = arr[now_i][now_j] + 1
        q.append([next_i, next_j])

for i in range(n*h):
    for j in range(m):
        if arr[i][j] == 0:      # 안익은 게 하나라도 있으면 실패
            ans = 0

print(ans-1)