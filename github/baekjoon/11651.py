N = int(input())
arr= []
for i in range(N):
    [x,y] = map(int, input().split(' '))
    arr.append([x,y])
arr2 = sorted(arr, key = lambda x:(x[1], x[0])) #lambda를 이용하여 x[1] 기준으로 정렬
#같은 숫자라면 두번째 조건을 더해서 결정 
for i in range(N):
    print(arr2[i][0], arr2[i][1])

