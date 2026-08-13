def solution(arr):
    if len(arr) == 1:
        return [-1]
    minidx = 0
    for i in range(len(arr)):
        if arr[i] < arr[minidx]:
                minidx = i
    arr.pop(minidx)
    return arr