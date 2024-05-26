def solution(n):
    answer = 0
    n = str(n)
    n = list(n)
    
    numbers = []
    for i in n:
        i = int(i)
        numbers.append(i)
        
    answer = sum(numbers)
    return answer