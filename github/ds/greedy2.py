
#문자열 02497이 주어졌을때 왼쪽 부터 계산한다 
#계산결과의 최대값을 구하라

#두수에 대하여 연산을 시행 둘 중 하나라도 1이하인 경우 덧셈을 이용
#두수 모두 2이상인 경우 곱셈 이용

s = input()
#처음 문자를 결과값에 대입
result = int(s[0])

for i in range(1,len(s)):
    num = int(s[i])
    if num <= 1 or result <= 1:
        result += num
    else :
        result *= num

print(result)

    
    