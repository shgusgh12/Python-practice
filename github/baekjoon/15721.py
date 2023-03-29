a = int(input()) #학생수
t = int(input()) #원하는 개수
m = int(input()) #원하는 문자 번호
arr =[]
n = 2

total = 0

while True:
    answer = 0
    arr += [0,1,0,1]
    for _ in range(n):
        arr.append(0)
    for _ in range(n):
        arr.append(1) 
       
    if t > (len(arr) // 2):
        n += 1
    else:
        for i in range(len(arr)):
            if arr[i] == m:
                answer+=1
                if answer == t:
                    total = i
                    break
    if total != 0:
        break

print(total % a)
            
            
