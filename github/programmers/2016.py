#윤년 2월 29일
def solution(a, b):
    arr = ['FRI', 'SAT','SUN','MON', 'TUE','WED','THU']
    
    #1월 1일 금요일
    #31일 달이면
    #앞까지의 달 더하고 나누기 7 -1한만큼 이동
    date = 0
    for i in range(1,a):
        if i == 2:
            date += 29
        elif i > 7:
            if i % 2 == 0:
                date += 31
            else : 
                date += 30
        elif i % 2 ==0:
            date += 30
        else :
            date += 31
    date += b
    cnt = date % 7
    cnt -= 1
    answer = arr[cnt]
    return answer
