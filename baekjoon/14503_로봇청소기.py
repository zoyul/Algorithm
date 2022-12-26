def func(now_i, now_j, d, ans):
    while 1:
        flag = False

        for k in range(4):
            next_d = (d + 3) % 4

            next_i = now_i + di[next_d]
            next_j = now_j + dj[next_d]
            d = next_d

            if (0 <= next_i < n and 0 <= next_j < m and MAP[next_i][next_j] == 0):
                MAP[next_i][next_j] = -1
                ans += 1
                now_i, now_j = next_i, next_j
                flag = True
                break

        if flag == False:
            if (0 <= next_i < n and 0 <= next_j < m and MAP[now_i-di[next_d]][now_j-dj[next_d]] == 1):
                return ans
            else:                   # 후진
                now_i -= di[d]
                now_j -= dj[d]

n, m = map(int, input().split())
i, j, direction = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]

di = [-1, 0, 1, 0]    # 0 3 2 1
dj = [0, 1, 0, -1]

MAP[i][j] = -1

print(func(i, j, direction, 1))