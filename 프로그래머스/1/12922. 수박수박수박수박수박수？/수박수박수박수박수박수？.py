def solution(n):
    res = []
    
    for i in range(n):
        res.append(' ')
        if i % 2 == 0:
            res[i] = '수'
        else:
            res[i] = '박'
            
    result = ('').join(res)
            
    return result