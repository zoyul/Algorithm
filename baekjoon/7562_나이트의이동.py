T = int(input())
for tc in range(T):
    n = int(input())
    now_i, now_j = map(int, input().split())
    goal_i, goal_j = map(int, input().split())
    MAP = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    di = [-2, -1, 1, 2, 2, 1, -1, -2]
    dj = [1, 2, 2, 1, -1, -2, -2, -1]

    # q 생성, 시작점 넣고 방문표시
    q = []
    q.append([now_i, now_j])
    visited[now_i][now_j] = 1
    
    # q가 비워질 때까8
    # 0 0
    # 7 0지
    while q:
        a = q.pop(0)
        now_i = a[0]
        now_j = a[1]

        for k in range(8):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어나면 무시
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
                continue
            # 지나갔던 점이면 무시
            if visited[next_i][next_j] != 0:
                continue
            q.append([next_i, next_j])
            visited[next_i][next_j] = visited[now_i][now_j] + 1

        # 목표에 도착하면 탈출
        if now_i == goal_i and now_j == goal_j:
            break



    print(visited[goal_i][goal_j]-1)