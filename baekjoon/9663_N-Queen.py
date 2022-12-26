# N-Queen
def check(x):                # 대각선으로 겹치는지
    for i in range(x):
        if abs(board[x] - board[i]) == x - i:
            return False
    return True

def dfs(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for i in range(n):
        if col[i] == 1:             # 같은 열에 있다면 무시
            continue
        board[row] = i
        if check(row) == 0:
            continue

        col[i] = 1
        dfs(row + 1)
        col[i] = 0

n = int(input())
col = [0] * n
board = [0] * n
cnt = 0
dfs(0)

print(cnt)