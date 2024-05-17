def solution(money):
    res = []
    
    cnt = int(money/5500)
    rem = money % 5500
    
    res.append(cnt)
    res.append(rem)
    
    return res