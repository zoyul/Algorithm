def cal(x, y, o):                   # 연산자로 연산하는 함수
    if o == '+':
        return (x + y)
    elif o == '-':
        return (x - y)
    elif o == '*':
        return (x * y)
    elif o == '%':
        if x >= 0:
            return (x // y)
        else:
            return (-((-x) // y))

def dfs(now_num, cnt):
    global max_num, min_num

    if cnt == n-1:      # 연산자로 쌍을 다 만들었으면 끝
        max_num = max(max_num, now_num)
        min_num = min(min_num, now_num)
        return

    for i in range(4):
        if op[i] == 0:          # 연산자가 남아있지 않으면 0
            continue

        op[i] -= 1
        dfs(cal(now_num, num[cnt+1], op_list[i]), cnt + 1)
        op[i] += 1                          # 다시 원상복구

n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
op_list = ['+', '-', '*', '%']

max_num = -2e29
min_num = 2e29

dfs(num[0], 0)

print(max_num)
print(min_num)