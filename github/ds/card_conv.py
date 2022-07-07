def card_conv(x:int, r:int) -> str:
    d= ''
    dchar = '0123456789ABCDEFGHIJKLMNOP'

    while x>0:
        d+=dchar[x%r]
        x //= r

    return d[::-1]


if __name__ == '__main__':
    while True:
        while True: 
            no = int(input())
            if no > 0:
                break
        while True:
            cd = int(input())
            if 2<= cd <= 36:
                break
        
        print(f'{cd}진수로 변환한 {no}는 {card_conv(no,cd)}')
        k = input()
        if k=='end':
            break