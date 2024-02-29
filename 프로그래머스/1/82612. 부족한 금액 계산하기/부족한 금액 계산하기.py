def solution(price, money, count):
    res = 0
    sum = 0
    
    for i in range(1, count + 1):
        sum += price * i
    
    res = sum - money
    if res < 0:
        return 0
    
    return res