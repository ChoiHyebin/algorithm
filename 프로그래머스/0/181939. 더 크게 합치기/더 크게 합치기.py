def solution(a, b):
    answer = ''
    
    a = str(a)
    b = str(b)
    
    if int(a+b) < int(b+a):
        answer = int(b+a)
    else:
        answer = int(a+b)
        
    return answer