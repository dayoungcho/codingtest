T = int(input())

for _ in range(1, T+1):
    N, K = map(int, input().split())  # N: 시험 친 과목 수, K: 성적표에 넣을 수 있는 과목 수
    score_list = list(map(int, input().split()))  # 성적 리스트
    score_list.sort()
    ans = sum(score_list[-K:])  # 성적 가장 높은 K개의 과목의 합

    print(f"#{_} {ans}")