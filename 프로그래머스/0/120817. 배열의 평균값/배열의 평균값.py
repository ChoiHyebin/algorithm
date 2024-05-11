def solution(numbers):
    answer = 0
    total = 0
    
    for i in numbers:
        total += i
    
    length = len(numbers)
    answer = total / length
    
    return answer