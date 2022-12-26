import sys

n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in range(n):
    sum_num = numbers[i]
    if sum_num == m:
        cnt += 1
    j = i + 1
    while sum_num < m and j < n:              # m되기 전까지
        sum_num += numbers[j]
        j += 1
        if sum_num == m:
            cnt += 1
            break

print(cnt)

# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))
#
# left, right = 0, 1
# cnt = 0
# while right <= n and left <= right:
#
#     sum_num = sum(numbers[left:right])
#
#     if sum_num == m:
#         cnt += 1
#         left += 1
#         right += 1
#
#     elif sum_num < m:
#         right += 1
#
#     elif sum_num > m:
#         left += 1
#
# print(cnt)