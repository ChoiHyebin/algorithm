def solution(t, p):
    res = 0
    
    t_len = len(t)
    p_len = len(p)
    
    for i in range(t_len-p_len+1):
        if int(t[i:i+p_len]) <= int(p):
            res += 1
    
    return res