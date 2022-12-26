def turn(i):                                        # 방향을 바꾸는
    global direction

    d = turn_direction.get(i)
    if d == 'D':
        direction = (direction + 1) % 4
    if d == 'L':
        direction = (direction - 1) % 4

n = int(input())
K = int(input())
MAP = [[0] * n for _ in range(n)]
for i in range(K):
    a, b = map(int, input().split())
    MAP[a-1][b-1] = 1
L = int(input())        # 방향횟수

di = [0, 1, 0, -1]  # 동 남 서 북
dj = [1, 0, -1, 0]

direction = 0
turn_cnt = []                       # 몇 번재에 턴할건지
turn_direction = {}                 # 어느 방향으로 턴할건지
for i in range(L):
    x, c = input().split()
    turn_cnt.append(int(x))
    turn_direction[int(x)] = c

# 시작점 세팅
now_i = 0
now_j = 0
MAP[now_i][now_j] = 2
cnt = 0
snake = []                  # snake의 위치를 다 넣어줄거임
snake.append([now_i, now_j])

while snake:
    now = snake[-1]
    now_i = now[0]
    now_j = now[1]

    if cnt in turn_cnt:
        turn(cnt)
        next_i = now_i + di[direction]
        next_j = now_j + dj[direction]

    else:
        next_i = now_i + di[direction]
        next_j = now_j + dj[direction]
    cnt += 1


    # 다음 칸이 벽이거나 나의 몸이면 멈추기
    if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
        break
    if MAP[next_i][next_j] == 2:
        break

    # 다음 칸이 사과면
    if MAP[next_i][next_j] == 1:
        MAP[next_i][next_j] = 2         # 뱀의 위치를 2로 표시 꼬리 그대로

    # 다음 칸이 사과가 아니면
    if MAP[next_i][next_j] == 0:
        MAP[next_i][next_j] = 2        # 앞으로 한 칸 가고
        tail = snake.pop(0)            # 맨 뒤에 있는거 즉 맨 처음에 넣은거 빼서 0으로 만들어줌
        MAP[tail[0]][tail[1]] = 0

    snake.append([next_i, next_j])

print(cnt)