r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
water = []      # 물의 위치 모두 잡아줌
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'S':     # 고슴도치
            start_i = i
            start_j = j
        if arr[i][j] == 'D':        # 굴
            goal_i = i
            goal_j = j
        if arr[i][j] == '*':
            water.append([i, j])


# 공백 q 설정, 시작점 넣고 , 방문 표시
q = []
q.append([start_i, start_j])
visited = [[0] * c for _ in range(r)]
visited[start_i][start_j] = 1
cnt = 1

di = [0, 0, -1, 1]
dj = [1, -1, 0, 0]

while q:
    now = q.pop(0)
    now_i = now[0]
    now_j = now[1]

    # water가 너무 많이 돔..
    if cnt <= visited[now_i][now_j]:            #  이걸로 해결 ㅎ~
        a = len(water)
        for x in range(a):
            now_water = water.pop(0)
            now_water_i = now_water[0]
            now_water_j = now_water[1]

            for l in range(4):
                next_water_i = now_water[0] + di[l]
                next_water_j = now_water[1] + dj[l]

                # 물이 채워나갈건데 맵을 넘어가거나, 돌이거나 굴이거나 이미 물이면 무시
                if next_water_i < 0 or next_water_i >= r or next_water_j < 0 or next_water_j >= c:
                    continue
                if arr[next_water_i][next_water_j] == 'X' or arr[next_water_i][next_water_j] == 'D':
                    continue
                if arr[next_water_i][next_water_j] == '*':
                    continue
                # 물이 갈 곳이 고슴도치가 현재 위치한 곳이라면 무시
                if visited[next_water_i][next_water_j] == visited[now_i][now_j]:
                    continue

                arr[next_water_i][next_water_j] = '*'
                water.append([next_water_i, next_water_j])

    for k in range(4):
        next_i = now_i + di[k]
        next_j = now_j + dj[k]

        # 범위 벗어나거나 지나갔던 점이거나 돌이면 무시 + 물이면 무시
        if next_i < 0 or next_i >= r or next_j < 0 or next_j >= c:
            continue
        if visited[next_i][next_j] != 0:
            continue
        if arr[next_i][next_j] == 'X':
            continue
        if arr[next_i][next_j] == '*':
            continue

        q.append([next_i, next_j])
        visited[next_i][next_j] = visited[now_i][now_j] + 1
        cnt = visited[next_i][next_j]


# 굴로 이동 못했으면 캌투스 아니면 시간 출력
if visited[goal_i][goal_j] == 0:
    print('KAKTUS')
else:
    print(visited[goal_i][goal_j]-1)
