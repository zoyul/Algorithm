import sys
import copy
from collections import deque

n = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

fish = [[] for _ in range(7)]
for i in range(n):
    for j in range(n):
        if MAP[i][j] >= 1 and MAP[i][j] <= 6:
            fish[MAP[i][j]].append((i, j))
        elif MAP[i][j] == 9:
            shark_i = i
            shark_j = j
shark_size = 2

def bfs(fish_i, fish_j, shark_i, shark_j, MAP, shark_size):              # 아기상어와 물고기 사이의 거리를 계산

    q = deque()
    q.append((shark_i, shark_j))
    visited = copy.deepcopy(MAP)
    visited[shark_i][shark_j] = -1

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while q:
        now_i, now_j = q.popleft()

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:      # 범위를 벗어났거나 지나갔거나 몸집이 나보다 크면 패스
                continue
            if visited[next_i][next_j] < 0:
                continue
            if MAP[next_i][next_j] > shark_size:
                continue

            q.append((next_i, next_j))
            visited[next_i][next_j] = visited[now_i][now_j] - 1

            if next_i == fish_i and next_j == fish_j:                       # 먹이까지의 위치를 구하면
                return abs(visited[fish_i][fish_j]) - 1

    return -1

def eat():
    pass

cnt = 0
eat_cnt = 0          # 몇  개 먹었는지
flag = 0
while 1:

    can = []
    min_dis = 1e7        # 가장 짧은 거리의 먹이 기록
    min_fish = []        # 최단거리가 똑같은 물고기들의 위치 저장
    if eat_cnt == shark_size:
        shark_size += 1
        MAP[shark_i][shark_j] += 1
        eat_cnt = 0
    for i in range(1, min(shark_size, len(fish))):     # 현재 아기상어가 먹을 수 있는 아기상어의 크기보다 작은 물고기가 있는지 확인
        if fish[i]:                                     # 먹을 수 있는 상어가 있으면 거리와 위치 비교
            for f in fish[i]:
                dis = bfs(f[0], f[1], shark_i, shark_j, MAP, shark_size)

                if dis > 0 and dis < min_dis:
                    min_dis = dis
                    can = []
                    can.append((f[0], f[1], dis, i))
                elif dis == min_dis:
                    can.append((f[0], f[1], dis, i))

    if can == []:
        print(cnt)
        exit()

    can.sort()

    target_i = can[0][0]
    target_j = can[0][1]
    dis = can[0][2]
    fish_size = can[0][3]

    fish[fish_size].remove((target_i, target_j))
    eat_cnt += 1
    MAP[target_i][target_j] = shark_size
    MAP[shark_i][shark_j] = 0
    shark_i, shark_j = target_i, target_j
    cnt += dis

print(cnt)
