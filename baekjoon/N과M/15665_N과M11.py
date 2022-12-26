N, M = map(int, input().split())
nums = list(map(int, input().split()))

result = set()

def dfs(lst):

    if len(lst) == M:
        result.add(tuple(lst))
        return

    for i in range(N):
        dfs(lst + [nums[i]])

dfs([])

for r in sorted(result):
    for s in r:
        print(s, end=" ")
    print()