def solution(myString):
    answer = []
    
    answer = myString.split('x')
    answer = [i for i in answer if i]
    
    answer = sorted(answer)
    
    return answer