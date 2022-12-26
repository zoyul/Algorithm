import sys

sys.setrecursionlimit(10**9)

def dfs(now, cost, max_cost):
    global result
    global ans

    if now == b:
        result = cost - max_cost
        ans = min(result, ans)
        return

    for next in graph[now]:
        next_to = next[0]
        next_cost = next[1]

        if check[next_to]:
            continue

        check[next_to] = 1
        dfs(next_to, cost+next_cost, max(max_cost, next_cost))
        check[next_to] = 0


n, a, b = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    n1, n2, w = map(int, sys.stdin.readline().split())
    graph[n1].append([n2, w])
    graph[n2].append([n1, w])

check = [0] * (n+1)
check[a] = 1
ans = 2e18
dfs(a, 0, 0)

print(ans)