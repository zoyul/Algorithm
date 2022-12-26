def dfs(password, c, v, idx):          # 자음 모음
    global result

    if len(password) == L:           # 길이가 l이 되면

        if c >= 2 and v >= 1:        # 자음, 모음 개수 만족하면 결과 추가 아니면 return
            print(password)
        else:
            return

    for i in range(idx, C):
        if visited[i] != 0:         # 지나갓던 곳이면 패스
            continue

        visited[i] = 1

        if ch[i] not in vowel:      # 자음이라면
            dfs(password + ch[i], c + 1, v, i)
            visited[i] = 0
        else:                   # 모음이라면
            dfs(password + ch[i], c, v + 1, i)
            visited[i] = 0

#  입력
L, C = map(int, input().split())
ch = input().split()
ch.sort()
vowel = ['a', 'e', 'i', 'o', 'u']
visited = [0] * C

password = ''
result = []
dfs(password, 0, 0, 0)