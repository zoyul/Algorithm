s = input()

i = 0
cnt = 0
# 문자열의 마지막 idx까지
while i < len(s):
    if s[i] == 'c':         # c라면 다음 문자를 검색하고 크로아티아면 2칸 이동
        i += 1
        if i < len(s) and (s[i] == '=' or s[i] == '-'):
            i += 1
    elif s[i] == 'd':
        i += 1
        if (i < len(s) and s[i] == 'z') and (i+1 < len(s) and s[i+1] == '='):
            i += 2
        elif i < len(s) and s[i] == '-':
            i += 1
    elif (i < len(s) and s[i] == 'l') and (i+1 < len(s) and s[i+1] == 'j'):
        i += 2
    elif s[i] == 'n' and (i+1 < len(s) and s[i+1] == 'j'):
        i += 2
    elif s[i] == 's' and (i+1 < len(s) and s[i+1] == '='):
        i += 2
    elif s[i] == 'z' and (i+1 < len(s) and s[i+1] == '='):
        i += 2
    else:
        i += 1
    cnt += 1

print(cnt)
