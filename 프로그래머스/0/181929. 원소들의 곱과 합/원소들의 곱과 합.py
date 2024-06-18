def solution(num_list):
    answer = 0
    multiply = 1
    
    for i in num_list:
        multiply *= i
    
    if multiply > sum(num_list) * sum(num_list):
        answer = 0
    elif multiply < sum(num_list) * sum(num_list):
        answer = 1
    
    return answer