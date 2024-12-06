from collections import deque


def solution(board):
    answer = 0
    q = deque()
    y = len(board)
    x = len(board[0])
    graph = [[-1 for _ in range(x)] for _ in range(y)]
    startx = 0
    starty = 0
    targetx = 0
    targety = 0
    for i in range(y):
        for j in range(x):
            if board[i][j] == 'R':
                startx = j
                starty = i
                
            if board[i][j] == 'D':
                graph[i][j] = 0
            if board[i][j] == 'G':
                targety = i
                targetx = j
    q.append([starty, startx])
    graph[starty][startx] = 0
    
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]
    
    while len(q) != 0:
        cur_y, cur_x = q.popleft()
        cnt = 0
        for move in range(4):
            next_y = cur_y 
            next_x = cur_x 
            # 장애물을 만나기 직전까지의 위치 계산
            while True:
                ny = next_y + dy[move]
                nx = next_x + dx[move]
                if ny < 0 or ny >= y or nx < 0 or nx >= x or board[ny][nx] == 'D':
                    if graph[next_y][next_x] == -1:
                        graph[next_y][next_x] = graph[cur_y][cur_x] + 1
                        q.append([next_y, next_x])
                    break
                next_y = ny
                next_x = nx
            
                    
                        
            
                        
                    
    return graph[targety][targetx] if graph[targety][targetx] != -1 else -1
                
            
    