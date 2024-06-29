def solution(a, b):
    answer = 0
    
    if int(str(a) + str(b)) < 2 * a * b:
        answer = 2 * a * b
    elif int(str(a) + str(b)) > 2 * a * b:
        answer = int(str(a) + str(b))
    
    return answer