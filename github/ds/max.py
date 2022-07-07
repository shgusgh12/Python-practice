from argparse import _MutuallyExclusiveGroup
from typing import Any, Sequence

from numpy import maximum

def max_of(a:Sequence) -> Any:
    '''시퀀스형 a 원소의 최댓값을 반환'''
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum

if __name__ == '__main__':  #max를 모듈로 사용했을때 if문 아래가 실행되지 않게 하기 위해
    # 이 프로그램이 실행될때 __name__은 __main__이 되고 아닐때는 __max__가
    print('최댓값을 구합니다.')
    num = int(input())
    x = [None] * num  #num 크기의 배열 지정 int arr[10] 같은 역할
 
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요:'))
    
    print(f'최댓값은 {max_of(x)}입니다')