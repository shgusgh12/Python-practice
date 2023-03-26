t = int(input())



for i in range(t):
    index0 = [0] * 41
    index1 = [0] * 41
    index0[0] = 1
    index0[1] = 0
    index1[0] = 0
    index1[1] = 1

    fibo = int(input())
    for j in range(2, fibo+1):
        if index0[j] == 0 and index1[j]==0:
            index0[j] = index0[j-2] + index0[j-1]
            index1[j] = index1[j-2] + index1[j-1]
    print(index0[fibo], index1[fibo])
    


        
    