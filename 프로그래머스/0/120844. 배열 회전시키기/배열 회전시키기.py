def solution(numbers, direction):
    answer = []
    
    if direction == 'right':
        numbers.insert(0, numbers[-1])
        numbers.pop()
        answer = numbers
    else:
        numbers.append(numbers[0])
        numbers.pop(0)
        answer = numbers
        
    return answer