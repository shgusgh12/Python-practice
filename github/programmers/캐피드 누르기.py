def solution(numbers, hand):
    answer = ''
    dial = {'1':[0,0], 
            '2':[0,1], 
            '3':[0,2],
            '4':[1,0],
            '5':[1,1],
            '6':[1,2],
            '7':[2,0],
            '8':[2,1],
            '9':[2,2],
            '*':[3,0],
            '0':[3,1],
            '#':[3,2]}
    left = dial['*']
    right = dial['#']
    for i in numbers:
        now = dial[i]
        if i in [1,4,7]:
            answer += 'L'
            left = now
        elif i in [3,6,9]:
            answer += 'R'
            right = now
        else:
            left = 0
            right = 0
        for a, b, c in zip(left, right, now):
            left += abs(a-c)
            right += abs(b-c)
            
        # 왼손이 더 가까운 경우
        if left < right:
            answer += 'L'
            left = now

        # 오른손이 더 가까운 경우
        elif left_d > right_d:
            answer += 'R'
            right_s = now

        # 두 거리가 같은 경우
        else:
            # 왼손잡이 경우
            if hand == 'left':
                answer += 'L'
                left_s = now

            # 오른손잡이 경우
            else:
                answer += 'R'
                right_s = now
            
    return answer    
        
        
