T = int(input())
for tc in range(T):
    n, m = map(int, input().split())        # 문서의 개수, 궁금한 문서 idx
    file = list(map(int, input().split()))

    q = []                                  # 문서의 idx 값이 나중에 필요하므로 idx와 같이 저장
    for i in range(n):
        q.append([file[i], i])

    v = [0] * n                         # 몇 번째로 빠졌는지 기록할 list

    cnt = 0
    while q:
        a = q.pop(0)
        cnt += 1                # 몇 번째로 뺐는지 확인하고 넣어줌
        v[a[1]] = cnt

        for i in range(len(q)):
            if q[i][0] > a[0]:                # 우선순위가 큰 게 있다면 뒤로 붙이고 cnt 다시 원위치
                q.append(a)
                cnt -= 1
                v[a[1]] = 0
                break

    print(v[m])