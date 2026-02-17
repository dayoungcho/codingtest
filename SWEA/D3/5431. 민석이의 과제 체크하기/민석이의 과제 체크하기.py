T = int(input())

for _ in range(1, T+1):
    N, K= map(int, input().split())  # N: 수강생의 수, K: 과제 제출한 사람 수

    assgn_lst = list(map(int, input().split())) # 과제 제출한 학생 번호 리스트
    student_lst = list(range(1,N+1)) # 전체 학생 번호 리스트

    for i in assgn_lst:
        student_lst.remove(i)  # 전체 학생 리스트에서 과제 제출한 학생 번호 빼기
    
    print(f"#{_} {' '.join(map(str, student_lst))}")