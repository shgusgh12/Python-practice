from max import max_of  #파일의 이름자체를 모듈로 사용가능하다 

number = 0
x = []

while True:
    s = input(f'x[{number}]값을 입력하세요:')
    if s == 'End':
        break
    x.append(int(s))
    number += 1

print(f'최댓값은 {max_of(x)}')