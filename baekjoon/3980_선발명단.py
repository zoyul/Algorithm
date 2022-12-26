import sys

c = int(sys.stdin.readline())
for _ in range(c):
    case = [list(map(int, sys.stdin.readline().split())) for _ in range(11)]

    position = [0] * 11             # 포지션을 채웠는지 체크하는 함수

    ans = 0
    def dfs(num):                   # player번호
        global ans

        if num > 10:                    # 끝까지 다 검사했다면
            ans = max(ans, sum(position))
            return

        for i in range(11):
            if position[i]:                 # 이미 채운 포지션이면 패스
                continue
            if case[num][i] == 0:           # 능력치가 0이면 패스
                continue

            position[i] = case[num][i]
            dfs(num + 1)
            position[i] = 0

    dfs(0)
    print(ans)