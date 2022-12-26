N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def dfs(lst):

    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return

    for i in range(N):
        dfs(lst + [nums[i]])

dfs([])