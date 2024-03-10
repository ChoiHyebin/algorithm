def solution(arr):
    res = []
    
    for i in range(len(arr)):
        res.append(arr[i])
        if [arr[i]] == arr[i+1:i+2]:
            res.pop()
    
    return res