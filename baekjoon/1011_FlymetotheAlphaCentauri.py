# 1~1 1번
# 2~2 2번

# 거리 이동최소횟수 (거리가 3, 4일땐 최소 3번, 5-6일땐 최소 4번 움직여야한다는 뜻)
# 3~4 3번
# 5~6 4번

# 7~9 5번
# 10~ 12 6번

# 13 ~ 15 7번

# 두 단계 씩 규칙이 반복
# i * (i+1) + 1 ~ (i+1) ** 2
# (i + 1) ** 2 + 1 + (i + 1) ** 2 + (i + 1)

T = int(input())
for tc in range(T):
    x, y = map(int, input().split())

    if (y-x) <= 2:                      # 거리 2이하인 건 그냥 출력
        print(y-x)
    else:
        i = 0
        flag = 1                    # 조건문을 멈출 조건
        while flag:
            i += 1
            for _ in range(2):                          # 2번씩 반복
                min_value = i * (i+1) + 1
                max_value = (i + 1) ** 2
                if (y - x) >= min_value:                # 범위안에 포함되면 끝!
                    if (y - x) <= max_value:
                        flag = 0
                        result = (i * 2) + 1

                min_value = (i + 1) ** 2 + 1
                max_value = (i + 1) ** 2 + (i + 1)
                if (y - x) >= min_value:
                    if (y - x) <= max_value:
                        flag = 0
                        result = (i + 1) * 2

        print(result)