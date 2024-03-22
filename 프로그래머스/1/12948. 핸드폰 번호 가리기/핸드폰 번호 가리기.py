def solution(phone_number):
    length = len(phone_number) - 4
    star = '*' * length
    tail = phone_number[-4:]
    
    res = star + tail
    
    return res