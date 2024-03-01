def solution(x):
    s = list(str(x))
    n = []
    
    res = True
    
    for i in s:
        n.append(int(i))
    
    if x % sum(n) == 0:
        res = True
    else:
        res = False
        
    return res