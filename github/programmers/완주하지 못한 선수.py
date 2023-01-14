
participant = ["fake", "kiki", "eden"]
completion = ["eden", "kiki"]
#zip 두개를 묶는 함수 p와 c를 묶음
#participant가 completion보다 하나 더 많아서 짝이 안맞는 하나가 답
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        if p != c:
            return p
    return participant.pop()

print(solution(participant, completion))