
board = input()

arr =[]
a= 'AAAA'
b= 'BB'
answer = []
for i in range(len(board)):
    if board[i] == '.':
        if len(arr) != 0:
            answer.append(''.join(arr))
        answer.append(board[i])
        arr = []
        continue  
    arr.append(board[i])
answer.append(''.join(arr))

for i in range(len(answer)):
    if answer[i] != '.':
        if len(answer[i]) % 2 == 0:
            answer[i] = (len(answer[i]) // 4) * a + (len(answer[i]) % 4)//2 * b
        else:
            print(-1)
            exit()
    
for i in answer:
    print(i, end='')
