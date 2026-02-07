# 글자판 생성
for _ in range(1, 11):
    t = int(input())  # 테스트 케이스 번호
    arr = []
    for r in range(100):
        row = list(input().strip())
        arr.append(row)

    N = len(arr[0])  # 글자판 크기

    idx = N  # 가장 긴 회문의 길이를 체크할 변수

    while idx > 1:
        # 가장 긴 회문부터 탐색, 회문 있으면 break
        for i in range(N):
            for j in range(N-idx+1):
                # 가로 회문부터
                candidate = arr[i][j:j+idx]
                is_palindrome = True
                for k in range(idx//2):
                    if candidate[k] != candidate[idx-k-1]:
                        is_palindrome = False
                        break
                else:
                    is_palindrome = True
                    ans = idx
                    break
                # 세로 회문
                candidate_2 = ''
                for l in range(idx):
                    candidate_2 += arr[j+l][i]
                is_palindrome = True
                for k in range(idx//2):
                    if candidate_2[k] != candidate_2[idx-k-1]:
                        is_palindrome = False
                        break
                else:
                    is_palindrome = True
                    ans = idx
                    break
            if is_palindrome:
                break
        if is_palindrome:
            break
        else:
            idx -= 1

    print(f"#{t} {idx}")