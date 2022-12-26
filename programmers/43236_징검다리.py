def solution(distance, rocks, n):

    rocks.sort()

    answer = 0
    left = 0
    right = distance
    while left <= right:
        mid = (left + right) // 2
        now = 0                 # 현재 위치
        cnt = 0                 # 제거한 바위의 개수
        min_distance = distance
        for rock in rocks:
            diff = rock - now               # 바위와 현재 위치 사이의 거리
            if diff < mid:                  # mid 보다 거리가 짧으면 바위 제거
                cnt += 1
            else:                           # mid 이상이면 현재 위치를 바위로
                now = rock
                min_distance = min(min_distance, diff)

        if cnt > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))