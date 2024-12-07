
import sys

input = sys.stdin.readline

a,b,c = map(int, input().split())


start = 1

for i in range(b):
    start = start * a % c

print(start)