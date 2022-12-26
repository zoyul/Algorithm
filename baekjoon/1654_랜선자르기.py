import sys

k, n = map(int, sys.stdin.readline().split())
lan = []
for _ in range(k):
    lan.append(int(sys.stdin.readline()))

left = 1
right = max(lan)

while left <= right:
    mid = (left + right) // 2

    result = 0
    for i in range(len(lan)):
        result += lan[i] // mid         # 랜선을 자름

    if result >= n:                     # 목표보다 많으면 더 크게 자르고 목표보다 적으면 작게 자름
        left = mid + 1
    else:
        right = mid - 1

print(right)