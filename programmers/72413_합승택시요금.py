import heapq

def solution(n, s, a, b, fares):

    adj = [[] for _ in range(n+1)]
    for n1, n2, w in fares:
        adj[n1].append((w, n2))
        adj[n2].append((w, n1))

    def dijkstra(start):
        INF = 1e9
        dist = [INF] * (n+1)
        dist[start] = 0

        hq = []
        heapq.heappush(hq, (0, start))

        while hq:
            now_cost, now = heapq.heappop(hq)

            for cost, to in adj[now]:
                if now_cost + cost < dist[to]:
                    dist[to] = now_cost + cost
                    heapq.heappush(hq, (dist[to], to))

        return dist

    dp = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    answer = 987654321
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))