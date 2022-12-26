# 터질 puyo가 있는지 체크
def check(i, j):
    # 공백 q 생성
    q = []
    visited = [[0] * 6 for _ in range(12)]
    q.append([i, j])
    visited[i][j] = 1

    cnt = []  # 같은 색을 가진 칸의 idx를 넣어줄 리스트
    cnt.append([i, j])

    while q:
        a = q.pop(0)
        now_i = a[0]
        now_j = a[1]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위 넘어가면 무시
            if next_i < 0 or next_i >= 12 or next_j < 0 or next_j >= 6:
                continue
            # 지나간 곳이면 무시
            if visited[next_i][next_j] != 0:
                continue
            # 다르면 무시
            if arr[next_i][next_j] != arr[now_i][now_j]:
                continue

            q.append([next_i, next_j])
            visited[next_i][next_j] = 1
            cnt.append([next_i, next_j])

    return cnt

# puyo를 터트림
def bomb(arr, c):
    global boom
    boom = 1
    # 같은 색이 4개 이상이면 터지기
    if len(c) >= 4:
        for p in c:
            arr[p[0]][p[1]] = '.'

# puyo가 터지면 다운
def down(arr):
    global flag
    flag = 0                                # 일단 0 만들고 밑에서 내려가면 1 만들기 안내려감녀 걍 0인거
    # 터진만큼내려와
    for x in range(11)[::-1]:
        for y in range(6):
            if arr[x][y] != '.':         # 나는 .이 아닌데 아래가 .이면 내려가(근데 .만큼 내려가야됨)
                if arr[x+1][y] == '.':
                    n = 1
                    flag = 1
                    while (x+n) <= 11 and arr[x+n][y] == '.':
                        arr[x+n][y] = arr[x+n-1][y]
                        arr[x+n-1][y] = '.'
                        n += 1

arr = [list(input()) for _ in range(12)]
result = 0
boom = 0
flag = 1
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

while flag:
    boom = 0
    # 맨 아래 맨 왼쪽부터 계속 탐색
    for i in range(12)[::-1]:
        for j in range(6):
            if arr[i][j] != '.':
                c = check(i, j)             # puyo 주변을 체크하고 4개면 터짐!! ( 터지면 boom함수가 boom변수를 1로 바꿔줌)
                if len(c) >= 4:
                    bomb(arr, c)
    if boom:             # 한 번이라도 터졌다면 내려가야지 (결과도 추가하고)
        result += 1
        down(arr)
    else:               # 안터졌다? 멈춰야지
        flag = 0

print(result)