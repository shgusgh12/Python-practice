import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = {}
for i in range(N):
    key = input().strip
    arr[key] = i
    arr[i] = key
for j in range(M):
    ans = input().strip()
    if ans.isdigit():      #숫자 구분해주는 함수
        print(arr[int(ans)-1])
    else:
        print(arr[ans]+1)
        
