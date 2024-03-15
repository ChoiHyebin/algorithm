def solution(n):    
    square = n ** 0.5
    
    if n % square == 0:
        res = (square + 1) ** 2
        return res
    else:
        return -1