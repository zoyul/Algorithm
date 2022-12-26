import sys
from collections import deque

def bomb():                 # 폭탄 설치
    for i in range(r):
        for j in range(c):
            MAP[i][j] = 'O'

def boom(q):                 # 폭탄 터짐!!

    while q:
        now = q.popleft()
        now_i = now[0]
        now_j = now[1]
        MAP[now_i][now_j] = '.'

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            if next_i < 0 or next_i >= r or next_j < 0 or next_j >= c:
                continue

            MAP[next_i][next_j] = '.'


r, c, n = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

n -= 1                                  # 어차피 처음 1초는 상관 x

for _ in range(n//2):                           # 폭탄이 설치된 곳을 다 q에 넣어줌
    q = deque()
    for i in range(r):
        for j in range(c):
            if MAP[i][j] == 'O':
                q.append([i, j])
    bomb()                                      # 폭탄설치, 폭탄 터지기
    boom(q)

for _ in range(n % 2):                          # 시간이 홀수면 설치한번더
    bomb()

for i in range(r):
    for j in range(c):
        print(MAP[i][j], end='')
    print()