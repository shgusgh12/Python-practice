str = list(input())
stack = []
res = 1
answer = 0
for i in range(len(str)):
    if str[i] == '(':
        res *= 2
        stack.append(str[i])
    elif str[i] == '[':
        res *= 3
        stack.append(str[i])
    elif str[i] == ')':
        if not stack or stack[-1] != '(':
            answer = 0
            break 
        if str[i-1] =='(':
            answer += res
        res //= 2
        stack.pop()
    elif str[i] == ']':
        if not stack or stack[-1] != '[':
            answer = 0
            break 
        if str[i-1] == '[':
            answer += res
        res //= 3
        stack.pop()
    
if stack:
    print(0)
else:
    print(answer)
# 스택
    



    
            

            

    



   
            
    