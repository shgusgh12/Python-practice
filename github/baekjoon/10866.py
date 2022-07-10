import sys
from collections import deque
 
d = deque()
input = sys.stdin.readline

n = int(input())
def pop_front():
    if empty()==0:
        print(-1)
    else:
        print(d.popleft)
def pop_back():
    if empty()==0:
        print(-1)
    else:
        print(d.pop)
def empty():
    if len(d)==0:
        print(1)
    else:
        print(0)
def push(y):
    d.append(y)
def push_front(y):
    d.appendleft(y)
def front():
    if len(d)==0:
        print(-1)
    else:
        print(d[0])
def back():
    if len(d)==0:
        print(-1)
    else:
        print(d[len(d)-1])
def size():
    print(len(d))
for _ in range(n):
    x = list(input().split())  #input을 list형태로 저장한다
    if x[0] == 'push_back':
        d.append(x[1])
    elif x[0] == 'push_front':
        d.appendleft(x[1])
    elif x[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif x[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    
    elif x[0] == 'front':
        front()
    elif x[0] == 'back':
        back()
    elif x[0] == 'size':
        size()
    elif x[0] == 'empty':
        empty()
    
    