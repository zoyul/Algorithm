import sys

n = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split()))

cards.sort()


def binary_search(num):
    left = 0
    right = n - 1

    while left <= right:
        mid = (left+right) // 2
        if num > cards[mid]:
            left = mid + 1
        elif num < cards[mid]:
            right = mid - 1
        else:
            break

    if cards[mid] == num:
        return 1
    else:
        return 0

answer = []
for i in range(M):
    answer.append(binary_search(check[i]))

print(" ".join(map(str, answer)))