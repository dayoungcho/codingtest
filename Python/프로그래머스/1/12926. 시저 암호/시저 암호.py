def solution(s, n):
    answer = ''
    lowers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppers = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(s)):
        if s[i] == ' ':
            answer += ' '
        elif s[i].islower():
            idx = lowers.index(s[i]) + n
            while idx >= len(lowers):
                idx -= len(lowers)
            answer += lowers[idx]
        else:
            idx = uppers.index(s[i]) + n
            while idx >= len(uppers):
                idx -= len(uppers)
            answer += uppers[idx]
    return answer