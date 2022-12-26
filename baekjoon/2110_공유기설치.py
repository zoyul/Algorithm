import sys

n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))

house.sort()

# 이진탐색을 할 대상은 집 사이의 거리
# 최소거리는 1, 최대거리는 처음과 끝
left = 1
right = house[-1] - house[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    now = house[0]
    cnt = 1

    # 공유기 설치
    for i in range(1, n):
        if house[i] >= now + mid:       # now는 현재 위치, mid는 공유기 거리
            cnt += 1
            now = house[i]

    # 공유기를 너무 많이 설치했다면 거리를 늘리고 적다면 거리를 줄이기
    if cnt >= c:
        left = mid + 1
        answer = mid
    elif cnt < c:
        right = mid - 1


print(mid)