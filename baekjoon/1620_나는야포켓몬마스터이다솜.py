import sys

n, m = map(int, sys.stdin.readline().split())
dict_poketmon = {}
poketmon = [0] * (n + 1)

for i in range(n):
    p = sys.stdin.readline().rstrip()
    dict_poketmon[p] = (i + 1)
    poketmon[i + 1] = p

for j in range(m):
    w = sys.stdin.readline().rstrip()
    if w.isdigit():         # 숫자면
        print(poketmon[int(w)])
    else:
        print(dict_poketmon.get(w))