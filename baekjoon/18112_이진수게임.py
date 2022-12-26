from collections import deque

start = int(input(), 2)                         # 10 진수로 바꾸기
goal = int(input(), 2)

check = [0] * 1500

# deque 선언, 시작점, 방문표시
q = deque()
q.append(start)
check[start] = 1

while q:
    if check[goal] != 0:
        break

    now = q.popleft()

    for k in range(3):
        if k == 0:                              # 한자리 숫자를 보수로 바꾸기
            l = len(bin(now))
            now = int(now)
            next_num = now
            for i in range(l-3):                         # 0인거 한자리 1로 바꾸기
                next_num = now ^ (1 << i)

                # 지나간 점이라면 , 범위 멋어나면
                if next_num <= 0 or next_num >= len(check):
                    continue
                if check[next_num] != 0:
                    continue

                q.append(next_num)
                check[next_num] = check[now] + 1

        elif k == 1:                            # 현재 수에 1 더하기
            next_num = now + 1
        elif k == 2:                            # 현재 수에서 1 빼기
            next_num = now - 1

        # 지나간 점이라면 , 범위 멋어나면
        if next_num <= 0 or next_num >= len(check):
            continue
        if check[next_num] != 0:
            continue

        q.append(next_num)
        check[next_num] = check[now] + 1

print(check[goal]-1)
