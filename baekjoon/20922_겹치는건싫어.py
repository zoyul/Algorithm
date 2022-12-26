n, k = map(int, input().split())
lst = list(map(int, input().split()))
check = [0] * (max(lst) + 1)                # 숫자가 몇 개 있는지 체크하는 배열
start, end = 0, 0
check[lst[start]] += 1

answer = 0
while end < n-1:
    end += 1
    check[lst[end]] += 1

    if check[lst[end]] > k:                        # 만약에 k 개수보다 많이 있으면
        while check[lst[start]] <= k:               # k이하가 될 때까지 start를 옮김
            check[lst[start]] -= 1
            start += 1
        check[lst[start]] -= 1
        start += 1

    answer = max(answer, (end - start + 1))

print(answer)