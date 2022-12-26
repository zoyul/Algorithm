N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = set()


def dfs(now, lst):

    if len(lst) == M:
        result.add(tuple(lst))
        return

    for i in range(now, N):
        dfs(i + 1, lst + [nums[i]])

dfs(0, [])

for r in sorted(result):
    for s in r:
        print(s, end=" ")
    print()