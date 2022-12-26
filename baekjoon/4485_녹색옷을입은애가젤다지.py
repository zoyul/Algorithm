import sys
import heapq

def dijkstra():
    visited = [[0] * n for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = MAP[0][0]
    visited[0][0] = 1

    hq = []
    heapq.heappush(hq, (dist[0][0], 0, 0))           # w, i, j

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    while hq:
        now_cost, now_i, now_j = heapq.heappop(hq)

        if now_i == n-1 and now_j == n-1:
            return dist[n-1][n-1]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            if visited[next_i][next_j] != 0:
                continue

            # 현재 좌표를 들러서 가는 것이 손해면 무시
            if dist[next_i][next_j] < MAP[next_i][next_j] + now_cost:
                continue

            dist[next_i][next_j] = MAP[next_i][next_j] + now_cost
            visited[next_i][next_j] = 1

            heapq.heappush(hq, (dist[next_i][next_j], next_i, next_j))

problem = 0
while 1:
    problem += 1
    n = int(input())
    if n == 0:
        break

    MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    INF = 9843572

    print(f'Problem {problem}: {dijkstra()}')