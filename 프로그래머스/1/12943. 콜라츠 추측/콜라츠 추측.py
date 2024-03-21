def solution(num):
    cnt = 0
    
    if num == 1:
        return 0
    
    while True:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num * 3 + 1
        cnt += 1
        
        if num == 1:
            break
    
    if cnt >= 500:
        return -1
    else:
        return cnt