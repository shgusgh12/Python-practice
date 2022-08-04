N, K = map(int, input().split())
arr = []
sum = []
cnt = 0
tmp = 0
for i in range(N):
    arr.append(int(input())) 
#띄어쓰기로 구분된 여러개의 숫자 입력시
#map을 이용한다 map함수는 type이 map이기에 int와 비교가 안된다
arr = sorted(arr, reverse=True) #reverse True 일때 내림차순으로 정렬
tmp = K
for i in range(N):
    if tmp // arr[i] > 0:
        cnt += tmp// arr[i]
        tmp = tmp % arr[i] 
print(cnt)
        