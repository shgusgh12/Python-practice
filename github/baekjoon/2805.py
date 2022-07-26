#매개변수 탐색

N , M = map(int, input().split(' '))

arr = map(int, input().split(' '))
arr = list(arr)
max = 0
for i in range(N):
    if arr[i] > max :
        max =arr[i]
start = 0  #나무를 얻을 수 있는 경우
end = max   #나무를 얻을 수 없는 경우
sum = 0

def check(height, arr, sum, M):
    
    for i in range(N):
        if arr[i] >= height:
            sum += arr[i] - height
    
    if sum >= M:
        return True
    else:
        return False

while start + 1< end:
    mid = (start + end)//2 
    
    if check(mid, arr, sum, M):
        start = mid   #mid를 체크했는데 sum이 더 큰 경우  
    else:
        end = mid   #sum 보다 작은경우
    
print(start)
