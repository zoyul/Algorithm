r, c = map(int, input().split())
MAP = [list(input()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
q = []
fire = []

for i in range(r):
    for j in range(c):
        if MAP[i][j] == 'J':
            q.append([i, j])
            visited[i][j] = 1
        if MAP[i][j] == 'F':
            fire.append([i, j])

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]
ans = 0

while q and ans == 0:
   # 불이 퍼지는거

    l = len(fire)
    for _ in range(l):
        now_fire = fire.pop(0)
        now_fire_i = now_fire[0]
        now_fire_j = now_fire[1]
        for k in range(4):
            next_fire_i = now_fire_i + di[k]
            next_fire_j = now_fire_j + dj[k]

            # 범위를 벗어나면, 벽이면 무시
            if next_fire_i < 0 or next_fire_i >= r or next_fire_j < 0 or next_fire_j >= c:
                continue
            if MAP[next_fire_i][next_fire_j] != '.':
                continue

            fire.append([next_fire_i, next_fire_j])
            MAP[next_fire_i][next_fire_j] = 'F'


    x = len(q)
    for _ in range(x):
        now = q.pop(0)
        now_i = now[0]
        now_j = now[1]

        # 지훈이가 움직이는거
        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나거나, 갈 수 없는 곳이면 무시, 지나갔던 곳이면 무시
            if next_i < 0 or next_i >= r or next_j < 0 or next_j >= c:
                ans = visited[now_i][now_j]
                break
            if MAP[next_i][next_j] != '.':
                continue
            if visited[next_i][next_j] != 0:
                continue

            q.append([next_i, next_j])
            visited[next_i][next_j] = visited[now_i][now_j] + 1


if ans == 0:
    print('IMPOSSIBLE')
else:
    print(ans)
# print(MAP)
# print(visited)


"""
10 10
#........#
#........#
#........#
#........#
#...J....#
#........#
#........#
#........#
#........#
FFFFFFFFFF
"""

""" # 3
4 4
###F
#J.#
#..#
#..#
"""

""" # 1
4 4
####
JF.#
#..#
#..#
"""

""" # im
5 5
#####
#...#
#.J.#
#...#
#####
"""

""" im
3 3
F.F
.J.
F.F
"""

""" #4
5 5
....F
...J#
....#
....#
...#.
"""