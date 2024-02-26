def solution(n):
    res = 0
    
    for i in range(1, n):
        if n % i == 1:
            res = i
            break;
        
    return res