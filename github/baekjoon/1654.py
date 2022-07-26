k , N = map(int, input().split(' '))
# x 값을 정해놓고 점점 늘려가면서 abcd 값을 더해 N에 가까워지면 출력
arr = []
for i in range(k):
    arr.append(int(input()))
start = 1
x = 0
min = 0
for i in range(k):
    if arr[i] > min:
        min = arr[i]
end = min
sum = 0
while start <= end:
    mid = (start + end) // 2
    
    for i in range(k):
        if arr[i] >= mid:
            sum += arr[i] // mid 
    if sum >= N:
        start = mid +1
    else:
        end = mid -1
    sum = 0
print (end)