n = input()
a = list(map(int, input().split()))
a.sort()
m = input()
k = list(map(int, input().split()))
def binary(x):
    start = 0
    end = len(a) -1
    while start <= end:
        mid = (start+end)//2
        if x==a[mid]:
            return 1
        if x>a[mid]:
            start = mid +1
        elif x < a[mid]:
            end = mid-1
for i in range(int(m)):
    if binary(k[i])==1:
        print(1)
    else:
        print(0)
           

