def t(x):
    h, m = map(int, x.split(':'))
    return 60 * h + m

import sys
s, e, q = sys.stdin.readline().split()

cnt = 0
student = {}

while 1:
    try:
        time, name = sys.stdin.readline().split()

        # 시작시간보다 댓글 시간이 작으면 저장
        if t(time) <= t(s):
            student[name] = 1
        elif t(time) >= t(e) and t(time) <= t(q) and student.get(name):
            cnt += 1
            student[name] = 0
    except:
        break

print(cnt)