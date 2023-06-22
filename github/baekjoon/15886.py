import sys
input = sys.stdin.readline

n = int(input())
move = input().rstrip()
answer = 0
for i in range(len(move)):
    if move[i] == 'E':
        if move[i+1] == 'W':
            answer +=1 

print(answer)