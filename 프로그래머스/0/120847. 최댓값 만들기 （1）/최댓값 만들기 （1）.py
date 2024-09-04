def solution(numbers):
    answer = 0
    
    numbers = sorted(numbers)
    numbers.reverse()
    
    answer = numbers[0] * numbers[1]
    return answer