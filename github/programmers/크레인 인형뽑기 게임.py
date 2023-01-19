def solution(board, moves):
    answer = 0
    stack = []
    length = max(moves)
    for i in moves:
        for j in range(length):
            if board[j][i-1] != 0:
                stack.append(board[j][i-1])
                board[j][i-1] = 0
                break
            else:
                continue
        if len(stack) > 1 and stack[-1] == stack[-2]:
            answer += 2
            stack.pop()
            stack.pop()
    
    return print(answer)

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]] 
moves = [1, 5, 3, 5, 1, 2, 1, 4]


solution(board, moves)