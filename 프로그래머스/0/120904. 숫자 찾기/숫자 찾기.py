def solution(num, k):
    answer = 0
    
    num = str(num)
    k = str(k)
    
    answer = num.find(k) + 1
    
    if k not in num:
        return -1
    
    return answer