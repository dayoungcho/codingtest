def solution(s):
    zeros = 0
    n_trans = 0
    while len(s) != 1:
        new_s = ''
        for i in s:
            if  i == '0':
                zeros += 1
            else:
                new_s += i
        s = format(len(new_s), 'b')
        n_trans += 1
    return [n_trans, zeros]