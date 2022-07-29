#블록 넣으면 2초 블록 꺼내서 놓으면 1초 블록은 1

N, M, B = map(int, input().split(' '))
arr = []
arr2 = [] 
for i in range(N):
    arr2 = map(int, input().split(' '))
    arr2 = list(arr2)
    arr.append([arr2])
val = min(map(min, arr))
min_val = min(val)
maxval = max(map(max, arr))
max_val = max(maxval)
tmp = min_val
answer = []
while True:
    T = 0 #블록을 인벤으로 
    a = 0 #인벤에서 밖으러
    for i in range(N):
        for j in range(M):
            if arr[i][j] >= tmp:
                T += arr[i][j] - tmp
                B += arr[i][j] - tmp
            elif arr[i][j] < tmp:
                a += tmp - arr[i][j]
                B -= tmp - arr[i][j]
    if B > 0 :
        answer.append(T*2 + a)     
    



            
                
            
    