def solution(answers):

    student = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]       # 수포자들의 답안지 리스트

    cnt = [0, 0, 0]

    for i in range(len(answers)):                           # 답이 맞으면 카운트를 1씩 증가시킴
        for j in range(3):
            if answers[i] == student[j][i % len(student[j])]:
                cnt[j] += 1

    max_cnt = max(cnt)
    answer = []
    for i in range(3):
        if cnt[i] == max_cnt:
            answer.append(i+1)

    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))