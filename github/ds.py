#n = int(input())

# for i in range(n):
#     if i % 2:
#         print('-', end='')
#     else:
#         print('+',end='')
# print()

for i in range(1, 10):
    for j in range(1,10):
        print(f'{i * j:3}', end=' ')  #3자리로 출력하기
    print()

n = int(input())
for i in range(n):
    for _ in range(n-i-1):
        print(' ',end='')
    for _ in range(i+1):
        print('*', end='')
    print()