from collections import defaultdict
import sys
input = sys.stdin.readline



while True:
    n,m = map(int, input().split())
    if n == 0 and m == 0: 
        break

    dict = defaultdict(int)        
    answer = []
    max = 0
    for i in range(n):
        arr = list(map(int, input().split()))
        for a in arr:
            if a in dict:
                dict[a] += 1
        
        for num in arr:
            if dict[num] > max:
                max = dict[num]
                answer = [num]
            elif dict[num] == max:
                answer.append(num)
    
    for k in answer:
        del dict[k]
    answer = []
    max = 0
    for k in dict:
        if dict[k] > max:
            max = dict[k]
            answer = [k]
        elif dict[k] == max:
            answer.append(k)
    print(*sorted(answer))

    

    

        
    
   