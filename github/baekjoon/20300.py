from collections import deque

n = int(input())

#운동기구 다 사용해야함
#고를때 최대 2개씩

#n이 짝수일때 홀수 일때 구분
answer = []
arr= list(map(int, input().split()))
arr.sort()

if n % 2 != 0:
    answer.append(arr.pop())

arr2 = arr[::-1]

for i in range(len(arr2)):
    answer.append(arr2[i] + arr[i])

print(min(answer))


