def solution(arr):
    min_num = 0
    res = []
    
    if len(arr) <= 1:
        res.append(-1)
        return res
    
    min_num = min(arr)
    arr.remove(min_num)
    
    return arr