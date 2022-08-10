import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = {}
for i in range(N):
    key = input().rstrip()
    arr[key] = i
    arr[i] = key
for j in range(M):
    ans = input().rstrip()
    if ans.isdigit():      #숫자 구분해주는 함수 input으로 받아도 숫자인지 아닌지 구분해줌
        print(arr[int(ans)-1])
    else:
        print(arr[ans]+1)
        
