# """
# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
# 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
# 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로, 그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
# """


def check(i, j):            # 좋아하는 친구가 주변에 몇 명 있는지
    global cnt_friend
    global cnt_blank

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for k in range(4):
        check_i = i + di[k]
        check_j = j + dj[k]

        if check_i < 0 or check_i >= n or check_j < 0 or check_j >= n:
            continue

        if classs[check_i][check_j] in friend[s-1]:       # 위아래왼오른쪽에 좋아하는 친구가 있다면
            cnt_friend += 1
        if classs[check_i][check_j] == 0:                   # 빈 칸이 있다면
            cnt_blank += 1

    option = [cnt_friend, cnt_blank, i, j]         # 친한 친구, 빈 칸, 위치
    options.append(option)                          # 선택지를 모두 넣어줌

    return

def cal(z, cnt):

    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]

    for k in range(4):
        check_i = i + di[k]
        check_j = j + dj[k]

        if check_i < 0 or check_i >= n or check_j < 0 or check_j >= n:
            continue

        if classs[check_i][check_j] in friend[z - 1]:  # 위아래왼오른쪽에 좋아하는 친구가 있다면
            cnt += 1

    return cnt

n = int(input())
friend = [[] for _ in range(n**2)]
student = []
for i in range(n**2):
    arr = list(map(int, input().split()))
    friend[arr[0]-1] = arr[1:]
    student.append(arr[0])

classs = [[0] * n for _ in range(n)]

for s in student:
    options = []
    for i in range(n):
        for j in range(n):
            if classs[i][j] == 0:               # 자리가 비어있다면
                cnt_friend = 0
                cnt_blank = 0

                check(i, j)                     # 어딜 앉을지 체크

    options.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))                  # 이제 정렬할거임 (기준: 좋아하는 친구, 빈칸, 행 번호, 열 번호)

    seat = options[0]
    classs[seat[2]][seat[3]] = s


ans = 0
for i in range(n):
    for j in range(n):
        z = classs[i][j]
        result = cal(z, 0)

        if result == 0:
            continue
        ans += 10 ** (result-1)

print(ans)