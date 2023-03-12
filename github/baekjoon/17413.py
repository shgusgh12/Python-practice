import sys
s = list(input())
   
cnt = 0
cnt2 = 0
word = ''


i = 0
while i < len(s):
    if s[i] == '<':
        i += 1
        while s[i] != '>':
            i += 1
        i += 1
    elif s[i].isalnum():  #숫자나 알파벳이면
        start = i
        while i < len(s) and s[i].isalnum():  
            i += 1
        tmp = s[start:i]
        tmp.reverse()  #reverse 함수 리스트만 사용가능
        s[start:i] = tmp
    else:
        i += 1

print(''.join(s))

