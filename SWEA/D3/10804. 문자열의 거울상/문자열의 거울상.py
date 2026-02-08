T = int(input())  #  테스트 케이스 수

for _ in range(1, T+1):
    mirror = input()
    mirrored = ''  # 거울에 비춘 문자열
    for i in mirror[::-1]:  # 거꾸로 순회
            if i == 'q':
                  mirrored += 'p'
            elif i == 'p':
                  mirrored += 'q'
            elif i == 'b':
                  mirrored += 'd'
            else:
                  mirrored += 'b'
    
    print(f"#{_} {mirrored}")
