N, M = map(int, input().split())

check = [0] * (N + 1)

def dfs(cnt, lst):

    if cnt == M:
        ans = " ".join(map(str, lst))
        print(ans)

    for i in range(1, N+1):
        if check[i]:
            continue

        check[i] = 1
        dfs(cnt + 1, lst + [i])
        check[i] = 0

dfs(0, [])