import sys
import math
input = sys.stdin.readline

n = int(input())


two = n // 2
remain = n % 2
answer = 0
for i in range(two, 0, -1):
    answer += math.factorial(i+remain) // (math.factorial(i) * math.factorial(remain))
    remain += 2

print((answer+1)%10007)
