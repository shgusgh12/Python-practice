n = int(input())
temp = input()
arr = []
stack = []
for i in range(n):
    arr.append(int(input()))

for i in temp:
    if ord(i) >= 65:
        stack.append(arr[ord(i)-ord('A')])
    else:
        x = stack.pop()
        y = stack.pop()
        if i == '*':
            stack.append(x * y)
        elif i == '+':
            stack.append(x + y)    
        elif i == '-':
            stack.append(y - x)    
        elif i == '/':
            stack.append(y / x)

print('%.2f' % stack[0])



