# import sys
# sys.setrecursionlimit(10**6)
#
# def dfs(now_i, now_j):
#     if now_i == n-1 and now_j == m-1:
#         return MAP[now_i][now_j]
#
#     if dp[now_i][now_j] != -1:
#         return dp[now_i][now_j]
#
#     ret = 0
#     for k in range(3):
#         next_i = now_i + di[k]
#         next_j = now_j + dj[k]
#
#         if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
#             continue
#
#         ret = max(ret, dfs(next_i, next_j) + MAP[now_i][now_j])
#     dp[now_i][now_j] = ret
#     return ret
#
# n, m = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(n)]
# dp = [[-1] * m for _ in range(n)]
#
# di = [1, 0, 1]
# dj = [0, 1, 1]
#
# print(dfs(0, 0))


""" 그냥 dp로만!! """

n, m = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# 초기값 설정
dp[0][0] = MAP[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + MAP[i][0]

for j in range(1, m):
    dp[0][j] = dp[0][j-1] + MAP[0][j]

# dp
for i in range(1, n):
    for j in range(1, m):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + MAP[i][j]

print(dp[n-1][m-1])