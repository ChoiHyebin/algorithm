def solution(my_string):
    answer = []
    
    numbers = []
    
    for i in my_string:
        if i.isdigit() == True:
            numbers.append(int(i))
    
    answer = sorted(numbers)
    
    return answer