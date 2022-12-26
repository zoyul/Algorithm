N, M = map(int, input().split())

def dfs(lst):

    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return

    for i in range(1, N+1):
        dfs(lst + [i])

dfs([])