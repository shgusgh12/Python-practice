
#개선 필요
def solution(array, commands):
    answer = []
    arr =[]
    c_length = len(commands)
    for i in range(len(commands)):
        for j in range(commands[i][1]-commands[i][0]+1):
            arr.append(array[j+1])
            arr.sort()
            answer.append(array[commands[i][2]])
            
    return answer
