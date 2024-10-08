def solution(my_string, s, e):
    answer = ''
    
    list = my_string[s:e+1]
    list = list[::-1]
    
    answer = my_string[:s] + list + my_string[e+1:]
    
    return answer