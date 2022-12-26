N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
check = [0] * N

def dfs(lst):

    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = 1
        dfs(lst + [nums[i]])
        check[i] = 0

dfs([])