
#개선 필요
#2차원 배열 구조 생각하기 
#효율성 체크 필요
def solution(array, commands):
    answer = []
    arr =[]
    c_length = len(commands)
    #2차원배열 1차원배열로
    for command in commands:
        for j in range(commands[i][1]-commands[i][0]+1):
            arr.append(array[j+1])
            arr.sort()
            answer.append(array[commands[i][2]])
            
    return answer
