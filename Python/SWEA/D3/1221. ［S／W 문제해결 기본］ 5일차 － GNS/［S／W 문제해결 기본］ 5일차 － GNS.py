planet_num = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())

for _ in range(1, T+1):
    N =  int(input()[3:])  # 테스트 케이스의 개수
    planet_arr = list(input().split())  # 행성 단어 리스트

    # 행성 단어를 숫자로 치환
    planet_as_num = []
    for i in range(N):
        planet_as_num.append(planet_num.index(planet_arr[i]))
        
    # 숫자 정렬 -> 정렬 함수 만들어서 써도 되지만 그냥 sort() 쓰겠습니다...
    planet_as_num.sort()
    
    # 다시 행성 단어로 치환
    sorted_planet = []
    for i in range(N):
        sorted_planet.append(planet_num[planet_as_num[i]])
        
    print(f"#{_}")
    print(' '.join(sorted_planet))