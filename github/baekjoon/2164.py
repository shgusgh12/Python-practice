from queue import Queue
N = int(input())
que = Queue()
for i in range(1, N+1):
    que.put(i)
while que.qsize() != 1:
    que.get()
    que.put(que.get())
    que.get()
print(que[0])



