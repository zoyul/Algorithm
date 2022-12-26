N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []

def dfs(now, lst):

    if len(lst) == M:
        print(" ".join(map(str, lst)))
        return

    record = 0                      # 이전 숫자를 기억
    for i in range(now, N):

        if nums[i] == record:
            continue

        record = nums[i]
        dfs(i, lst + [nums[i]])


dfs(0, [])