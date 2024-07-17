def solution(myString):
    answer = ''
    
    for i in myString:
        if i == 'a':
            i = i.upper()
        elif i == 'A':
            i = i
        else:
            i = i.lower()
        answer += i
        
    return answer