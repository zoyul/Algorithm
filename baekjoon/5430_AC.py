import sys

T = int(input())
for tc in range(T):
    p = sys.stdin.readline().rstrip()     # 수행할 명령어
    n = int(sys.stdin.readline().rstrip())        # 배열에 들어있는 수의 개수
    arr = sys.stdin.readline().rstrip()[1:-1]

    if n == 0:
        arr = []
    else:
        arr = list(map(int, arr.split(',')))

    result = arr
    R_cnt = 0
    for order in p:
        if order == 'R':
            R_cnt += 1
            if R_cnt % 2 == 0:              # R 짝수게 있으면 안뒤집힌거
                R_cnt = 0
        elif order == 'D':
            if len(result) == 0:
                result = 'error'
                break
            if R_cnt:                 # 뒤집혀있다면 뒤에서 뺌
                result.pop()
            elif R_cnt == 0:
                result.pop(0)

    if result != 'error':
        if R_cnt:
            result = result[::-1]
        result = ('[' + ','.join(map(str, result)) + ']')

    print(result)


"""
3
RR
2
[30, 40]
RRRRRRRRR
0
[]
DDR
2
[1,2]
"""