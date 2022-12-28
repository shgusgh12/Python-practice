def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            answer.append(numbers[i] + numbers[j])
    ans = set(answer)
    ans1 = list(ans)
    ans1.sort()
    return ans1
