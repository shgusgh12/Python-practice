N , M = map(int, input().split(' '))

arr = map(int, input().split(' '))
arr = list(arr)
arr2 = sorted(arr)
sum = 0
h = 1

while True:
    for i in range(N):
        sum += arr2[i] - h
    if sum == M :
        break
    else:
        h+=1
        sum=0 

print(h)