n = int(input())
arr =[]
dict = {}

cnt = 0

for i in range(n):
    s = input()
    idx = s.index('.') 
    if s[idx+1:len(s)] in dict:
        dict[s[idx+1:len(s)]] += 1
    else: 
        dict[s[idx+1:len(s)]] = 1
answer = sorted(dict.items())
answer = list(answer)
for i in range(len(answer)):
    print(answer[i][0], answer[i][1]) 
        
        