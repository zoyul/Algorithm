n = int(input())
day = []
money = []
for _ in range(n):
    t, p = map(int, input().split())
    day.append(t)
    money.append(p)

dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i + day[i] > n:              # 지금 날짜에 일을 하려는데 그 일이 마지막 날을 넘어서면 상담을 못하니까 이전 dp 값을 그대로 가져옴
        dp[i] = dp[i+1]
    else:                           # 그날 상담을 할지, 그날 일을 안하면 얼마나 가질 수 있는지 비교
        dp[i] = max(money[i] + dp[i+day[i]], dp[i+1])

print(dp[0])
