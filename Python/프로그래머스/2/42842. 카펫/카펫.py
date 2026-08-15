def solution(brown, yellow):
    x = 3  # 가로
    y = 3  # 세로
    flag = True
    while flag:
        if brown == (x + y - 2) * 2 and yellow == (x-2) * (y-2):
            answer = [x,y]
            break
        else:
            if x > y:
                y += 1
            else:
                x += 1
                y = 3
                
    return answer