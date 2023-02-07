n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

#파이썬의 sort 라이브러리는 nlogn이기 때문에 
#계수정렬과 같은 특별한 상황이 아니면 기본 라이브러리 사용
a.sort()
b.sort(reverse=True)
answer = 0 

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else: 
        break

for i in range(len(a)):
    answer += a[i]

print(answer)