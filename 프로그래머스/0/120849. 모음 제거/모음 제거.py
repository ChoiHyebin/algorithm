def solution(my_string):
    answer = ''
    
    gather = ['a', 'e', 'i', 'o', 'u']
    
    for i in my_string:
        if i in gather:
            i = ''
        answer += i
            
    return answer