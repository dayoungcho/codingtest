def solution(code):
    mode = 0
    ret = ''
    for i in range(len(code)):
        if mode == 0:
            if code[i]=="1":
                mode = 1
            else:
                if i%2==0:
                    ret += code[i]
            continue
        if mode == 1:
            if code[i]=="1":
                mode = 0
            else:
                if i%2==1:
                    ret += code[i]
            continue
    if ret == '':
        ret = "EMPTY"
    return ret



# 천재풀이

def solution(code):
    return "".join(code.split("1"))[::2] or "EMPTY"