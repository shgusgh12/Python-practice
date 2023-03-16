import sys

n = int(sys.stdin.readline())

ml = list(map(int, input().split()))
ml.sort(reverse=True)

answer = ml[0]

for i in range(1,n):
    answer += ml[i] / 2

print(answer)