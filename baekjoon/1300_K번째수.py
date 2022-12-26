n = int(input())
k = int(input())

left = 1
right = k
answer = 0

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for i in range(1, n+1):
        cnt += min(mid//i, n)       # mid 이하의 i의 배수, 최대 n

    if cnt >= k:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1

print(answer)

"""
예를 들어 10 * 10에서 20보다 작거나 같은 수

1*1~1*10
2*1~2*10
3*1~3*6

10*1~10*2

즉, 20을 행으로 나눈 몫

20//1: 10개 
20//2: 10개
20//3: 6개

20//10: 2개
"""
