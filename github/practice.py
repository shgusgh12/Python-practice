a = 100, 5 , 'k'
print('"더이상 카레먹기 싫어요"')
#is 연산자 
#== 연산자는 값을 비교하는 연산자
#값을 비교하는 것이 아니라 변수가 가리키고 있는 곳 비교
a = [1,2,3,4,5]
b = a
c = [1,2,3,4,5]

print('a is b = ', a is b)
print('a is c= ', a is c)
print('b is c = ',b is c)
a = "korea"
b += "!"
c = b[:-1]
#슬라이싱 하는 순간 새롭게 할당된다.
print ('a is c =', a is c)

#elif else 조건문 
age = 20

if age < 30:
    print("청년이에요")
elif age < 60:
    print("중년")
else:
    print("노년")

#for 반복문
for asdf in range(10):
    print(asdf)