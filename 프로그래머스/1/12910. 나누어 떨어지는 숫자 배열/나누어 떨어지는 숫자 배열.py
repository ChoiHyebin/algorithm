def solution(arr, divisor):
    res = []
    
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            res.append(arr[i])
    res = sorted(res)
    
    if len(res) == 0:
        res.append(-1)
        
    return res