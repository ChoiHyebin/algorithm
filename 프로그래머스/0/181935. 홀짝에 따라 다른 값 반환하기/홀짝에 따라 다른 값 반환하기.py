def solution(n):    
    answer = 0
    
    odd = []
    even = []
    
    for i in range(1, n + 1):
        if i % 2 == 1:
            answer = 0
            odd.append(i)
            answer = sum(odd)
        elif i % 2 == 0:
            answer = 0
            even.append(i)
            for j in even:
                answer += j * j
        
    return answer