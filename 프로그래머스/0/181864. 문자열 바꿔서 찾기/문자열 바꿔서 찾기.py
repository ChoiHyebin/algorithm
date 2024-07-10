def solution(myString, pat):
    answer = 0
    str = ''
    
    for i in myString:
        if i == 'A':
            i = 'B'
            str += i
        elif i == 'B':
            i = 'A'
            str += i
            
    if pat in str:
        answer = 1
    else:
        answer = 0
        
    return answer