F, S, G, U, D = map(int, input().split())

floor = [0] * (F+1)

q = []
q.append(S)
floor[S] = 1

df = [U, -D]            # 올라가는거 내려가는거

while q:
    now = q.pop(0)

    for k in range(2):
        next = now + df[k]

        if next <= 0 or next > F:           # 층 벗어나면 무시
            continue
        if floor[next] != 0:        # 갔던 곳이면 무시
            continue

        floor[next] = floor[now] + 1
        q.append(next)

if floor[G] == 0:
    print('use the stairs')
else:
    print(floor[G]-1)