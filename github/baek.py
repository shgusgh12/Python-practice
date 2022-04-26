

n , k = map(int,input().split())
def fact(a):
    if a==0:
        return 1
    if a == 1 :
        return 1
    else :
        return a * fact(a-1)

sum = fact(n)//(fact(n-k)*fact(k))  
print(sum)

