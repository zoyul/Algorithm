n = int(input())
room = list(map(int, input().split()))
a, b = map(int, input().split())    # 총감독관, 부감독관

total = n   # 일단 방 개수만큼 총감독관 필요하니까

# 총감독관님이 관리하는 학생수 제외
for i in range(n):
    room[i] -= a

# 부감독관 계산
for i in range(n):
    if room[i] > 0:
        if room[i] % b == 0:
            total += room[i]//b
        else:
            total += room[i] // b + 1

print(total)