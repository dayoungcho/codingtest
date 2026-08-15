def solution(sizes):
    answer = 0
    vertical = 0
    horizontal = 0
    for size in sizes:
        size = sorted(size)
        if size[0] > vertical:
            vertical = size[0]
        if size[1] > horizontal:
            horizontal = size[1]
    answer = vertical * horizontal
    return answer