def solution(n):
    s = str(n)
    arr = sorted(list(s))
    arr.reverse()
    
    arr = "".join(arr)
    res = int(arr)
    
    return res