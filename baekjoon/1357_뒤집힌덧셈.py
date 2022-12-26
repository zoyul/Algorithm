def reverse(num):
    reverse_num = str(num)[::-1]            # 숫자를 받아서 str으로 바꾼 후 뒤집음
    return (int(reverse_num))               # 정수로 반환

a, b = map(int, input().split())
result = reverse(reverse(a) + reverse(b))
print(result)