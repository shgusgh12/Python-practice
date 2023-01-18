location = input()
row = int(location[1])
column = int(ord(location[0])) - int(ord('a')) + 1

move = [(-2,-1), (-2,1), (-1,2), (-1,-2), (1,2), (1,-2), (2,1), (2,-1)]

#8가지의 이동이 matrix 안에 있는지 확인
result = 0
for step in move:
    x= row + step[0]
    y= column + step[1]

    if x >= 1 and x <= 8 and y >= 1 and y <= 8:
        result +=1 

print(result)