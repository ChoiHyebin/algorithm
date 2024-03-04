def solution(n):
    measure = []
    total = 0
    
    for i in range(1, n+1):
        if n % i == 0:
            measure.append(i)
    total = sum(measure)
    return total