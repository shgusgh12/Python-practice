quack = 'quack'
duck = input()
visited = [False] * len(duck)
cnt = 0
answer = 0
def find(start):
    global cnt 
    j = 0
    for i in range(start, len(duck)):        
        if duck[i] == quack[j] and not visited[i]:
            visited[i] = True
            if duck[i] == 'k':
                j = 0
                cnt += 1
            else:
                j += 1
        



if len(duck) % 5 != 0:
    print(-1)
    exit()

    


for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        find(i)
        if cnt != 0:
            answer += 1

if answer == 0 or not all(visited):
    print(-1)
else:
    print(answer)
            
    
 