n = int(input())
arr = list(map(int, input().split()))
m = int(input())

left = 1
right = max(arr)
total = 0

if sum(arr) < m:
    print(max(arr))
else:
    while left <= right:
        middle = (left + right)//2

        # 이진탐색을 기준으로 계산
        total = 0
        for i in arr:
            if i >= middle:
                total += middle
            else:
                total += i

        # 전체가 상한가보다 크면 범위는 작은숫자로
        if total > m:
            right = middle - 1
        elif total < m:
            left = middle + 1
        else:
            break

    if total > m:
        print(middle-1)
    else:
        print(middle)