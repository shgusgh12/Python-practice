j = input()
c =[]
for i in range(int(j)):
    c.append(input())
lst = list(set(c))   #set으로 바꿔서 중복제거
lst2 = []
for i in lst:
    lst2.append((len(i), i))
lst2.sort()   #len 오름차순으로 sorting
for j, k in lst2:
    print (k)