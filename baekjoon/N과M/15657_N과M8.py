N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(now, lst):

    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return

    for i in range(now, N):
        dfs(i, lst + [nums[i]])

dfs(0, [])