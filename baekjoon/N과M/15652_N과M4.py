N, M = map(int, input().split())

def dfs(now, lst):

    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return

    for i in range(now, N+1):
        dfs(i, lst + [i])

dfs(1, [])