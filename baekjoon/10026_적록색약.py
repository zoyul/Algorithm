# 적록색약아닌경우
def color(x, y, num):
    q = []
    q.append([x, y])
    visited[x][y] = num

    while q:
        a = q.pop(0)
        now_i = a[0]
        now_j = a[1]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 일단범위 넘어가면 무시
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            # 방문했던 곳이면 무시
            if visited[next_i][next_j] != 0:
                continue

            # 만약에 지금 나랑 다음 색이랑 같다면
            if arr[now_i][now_j] == arr[next_i][next_j]:
                visited[next_i][next_j] = num
                q.append([next_i, next_j])

# 적록색약인경우
def colorx(x, y, num):
    q = []
    q.append([x, y])
    visited2[x][y] = num

    while q:
        a = q.pop(0)
        now_i = a[0]
        now_j = a[1]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 일단범위 넘어가면 무시
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            # 방문했던 곳이면 무시
            if visited2[next_i][next_j] != 0:
                continue

            # 만약에 지금 나랑 다음 색이랑 같거나 R, G 일 때
            if arr[now_i][now_j] == 'G' or arr[now_i][now_j] == 'R':
                if arr[next_i][next_j] == 'G' or arr[next_i][next_j] == 'R':
                    visited2[next_i][next_j] = num
                    q.append([next_i, next_j])
            elif arr[now_i][now_j] == arr[next_i][next_j]:
                visited2[next_i][next_j] = num
                q.append([next_i, next_j])

n = int(input())
arr = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
visited2 = [[0]*n for _ in range(n)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

# 적록색약이 아닌 경우
num = 1
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            color(i, j, num)
            num += 1

print(num-1, end = ' ')

# 적록색약인 경우
num = 1
for i in range(n):
    for j in range(n):
        if visited2[i][j] == 0:
            colorx(i, j, num)
            num += 1

print(num-1)