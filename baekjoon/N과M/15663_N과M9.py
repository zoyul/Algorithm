N, M = map(int, input().split())
nums = list(map(int, input().split()))
check = [0] * N

result = set()

def dfs(lst):

    if len(lst) == M:
        result.add(tuple(lst))
        return

    for i in range(N):
        if check[i]:
            continue

        check[i] = 1
        dfs(lst + [nums[i]])
        check[i] = 0

dfs([])

for r in sorted(result):
    for s in r:
        print(s, end=" ")
    print()