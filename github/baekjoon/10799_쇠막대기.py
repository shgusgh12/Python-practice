stick = input()
stack = []
answer = 0
old = ''
# )가 왔을때 스택의 상위값을 생각해서 구분하기
for i in stick:
    if i == '(':
        stack.append(i)
    elif i == ')' and old == '(':
        stack.pop()
        answer+= len(stack)
        
    elif i == ')' and old == ')':
        stack.pop()
        answer += 1
    old = i
print(answer)
     
        
        
            