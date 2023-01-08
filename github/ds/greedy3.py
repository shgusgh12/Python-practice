#모험가 그룹 
n = int(input())
arr = list(map(int, input().split()))
arr.sort() #공포도를 낮은 수 부터 정렬한다
count = 0 #현재 그룹에 포함된 모험가의 수
answer = 0 # 총 그룹의 수
for i in arr:  
    count += 1   
    if count >= i:  #현재 그룹의 수가 현재 검사하는 공포도 이상인 경우 그룹을 결성함
        answer += 1
        count = 0
    
print(answer)