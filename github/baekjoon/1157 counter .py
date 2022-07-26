from collections import Counter  
c = Counter(input().upper())
sum = []
for i in c.keys(): 
    if c[i] == max(c.values()):
        sum.append(i)

if len (sum) > 1:
    print('?')
else:
    print(sum[0])

#counter & dict 이용 str 개수세기