#약수를 제곱근의 반까지 for문 돌려서 구하기 
#시간초과일어남

def solution(number, limit, power):
    answer = 0
    arr=[0 for _ in range(number)]
    for i in range(1,number+1):
        count = 0
        for j in range(1,int(i**(1/2))+1):
            if i%j == 0:      
                count += 1
                if (j != (i//j)):
                    count += 1
        arr[i-1] = count
    for i in range(number):
        if arr[i] > limit:
            arr[i] = power
    for i in range(number):
        answer += arr[i]
    return answer
