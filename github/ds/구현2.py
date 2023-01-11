n = int(input())
x =0
y = 0
z = 0
answer = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                answer +=1
print(answer)