n, d, k, c = map(int, input().split())  # n: 접시수, d: 초밥 가짓수 k: 연속접시수 c:쿠폰번호
sushi = []
for i in range(n):
    sushi.append(int(input()))
sushi *= 2      # idx 계산 귀찮으니까 걍 아예 크게 만들어버리자
# 일단 0번째부터 k번째까지
left = 0
right = k

max_sushi = 0
options = []
# 시작이 마지막 idx일때까지만 돌거임
while left < n:
    option = set(sushi[left:right])
    left += 1
    right += 1
    max_sushi = max(max_sushi, len(option))
    if len(option) >= max_sushi:
        options.append(option)

# print(options)
ans = k
for option in options:
    if len(option) == k:                # k만큼 먹었고 쿠폰이 안에 없으면
        if c not in option:
            ans = k + 1
            break
    else:
        if c not in option:
            ans = len(option) + 1
        else:
            ans = max_sushi


print(ans)