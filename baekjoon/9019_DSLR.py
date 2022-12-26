from collections import deque

def cal(num, x):
    if x == 0:                                  # D
        result = num*2
        if result > 9999:
            result %= 10000
    elif x == 1:                                # S
        if num == 0:
            result = 9999
        else:
            result = num - 1
    elif x == 2:                                # L
        result = (num * 10) % 10000 + num // 1000
        # result = (num % 1000) * 10 + num // 1000

    elif x == 3:                                # R
        result = (num % 10) * 1000 + num // 10

    return result

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())

    check = [''] * 10001
    DSLR = ['D', 'S', 'L', 'R']

    # 공백 q 생성, 시작점 표시
    q = deque()
    q.append(a)
    check[a] = '1'

    while q:
        if check[b] != '':
            break

        now = q.popleft()

        for k in range(4):
            next = cal(now, k)

            # 지나갔던 점이면 무시
            if check[next] != '':
                continue

            check[next] = check[now] + DSLR[k]
            q.append(next)

    print(check[b][1:])