# import sys
# import heapq
#
# def prim():
#     MST = [0] * m
#
#     hq = []
#     heapq.heappush(hq, (0, 0))
#     ans = 0
#
#     while hq:
#         now_cost, now = heapq.heappop(hq)
#         if MST[now] != 0:
#             continue
#         ans += now_cost
#         MST[now] = 1
#
#         for cost, idx in adj[now]:
#             if not MST[idx]:
#                 heapq.heappush(hq, (cost, idx))
#
#     return ans
#
# while 1:
#     m, n = map(int, input().split())
#     if m == 0 and n == 0:
#         break
#
#     adj = [[] for _ in range(m)]
#
#     total = 0
#     for _ in range(n):
#         n1, n2, w = map(int, sys.stdin.readline().split())
#         adj[n1].append((w, n2))
#         adj[n2].append((w, n1))
#         total += w
#
#     print(total - prim())


import sys

# def find(x):
#     if x == p[x]:
#         return x
#     px = find(p[x])
#     p[x] = px
#     return px

def find(x):
    while p[x] != x:
        x = p[x]
    return x


def union(x, y):
    px = p[x]
    py = p[y]
    p[py] = px

while 1:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break

    p = list(range(m))
    edges = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    edges.sort(key=lambda x: x[2])

    total = 0
    for edge in edges:
        total += edge[2]

    cnt = 0
    ans = 0
    for x, y, w in edges:
        if find(x) != find(y):
            ans += w
            cnt += 1
            union(x, y)
        if cnt == m:
            break

    print(total - ans)
    print(edges)