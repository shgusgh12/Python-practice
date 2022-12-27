#문자열 변환하는 replace함수 사용
#dictionary로 문자 관리
#for문 in 사용
def solution(s):
    arr = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

    for i in arr:
        s = s.replace(i, arr[i])
    answer = int(s)
    return answer

