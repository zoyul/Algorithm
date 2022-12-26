def solution(n, times):

    left = 0
    right = max(times) * n
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        people = 0

        for time in times:
            people += mid // time

        if people >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

print(solution(6, [7, 10]))

"""
https://happy-obok.tistory.com/10
"""