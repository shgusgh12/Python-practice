def solution(t, p):
    answer = 0
    arr =[]
    n = ''
    for i in range(0,len(t)):
        if len(p)+i <= len(t):
            for j in range(i,len(p)+i):        
                n += t[j] 
            arr.append(n)
            n = ''
    for i in range(len(arr)):
        if int(arr[i]) <= int(p):
            answer+=1
    return answer
