import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

answer = len(graph[1])          # 먼저 상근이의 친구들 초대

# 상근이의 친구들 초대 체크
check = [0] * (n+1)
check[1] = 1
for f in graph[1]:
    check[f] = 1

# 친구의 친구 체크
for f in graph[1]:
    for i in graph[f]:
        if not check[i]:
            check[i] = 1
            answer += 1

print(answer)