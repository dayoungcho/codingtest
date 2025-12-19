def solution(s):
    nums = list(map(int, s.split()))
    a = min(nums)
    b = max(nums)
    answer = str(a) + " " + str(b)
    return answer