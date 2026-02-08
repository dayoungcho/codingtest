T = int(input())  #  테스트 케이스 수

for _ in range(1, T+1):
    # 글자판 만들기
    arr = []
    for r in range(5):
        row = list(input())
        arr.append(row)
    
    # 단어의 최대 길이 구하기
    max_len = max([len(row) for row in arr])

    # 열-행 순으로 순회하며 세로로 읽은 글자 출력하기
    ans = ''
    for c in range(max_len):
        for r in range(5):
            if len(arr[r]) > c:
                ans += arr[r][c]

    print(f"#{_} {ans}")