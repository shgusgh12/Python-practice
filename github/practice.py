import sys

def hanoi(n, source, auxiliary, target):
    if n > 0:
        # 원반 n-1개를 auxiliary로 옮김
        hanoi(n-1, source, target, auxiliary)
        
        # 가장 큰 원반을 target으로 옮김
        print(f"{source}에서 {target}로 원반 {n}을(를) 이동")
        
        # auxiliary에 있는 원반 n-1개를 target으로 옮김
        hanoi(n-1, auxiliary, source, target)

  
n = int(sys.argv[1])  # 첫 번째 명령어 인자를 원반 개수(n)로 저장
source = "A"  # 출발
auxiliary = "B"  # 보조
target = "C"  # 목표

# 하노이 탑 알고리즘 호출
hanoi(n, source, auxiliary, target)