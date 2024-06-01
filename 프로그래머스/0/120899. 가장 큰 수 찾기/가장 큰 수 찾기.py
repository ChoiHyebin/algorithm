def solution(array):
    answer = []
    
    n = 0
    for i in range(len(array)):
        if array[i] == max(array):
            n = i
    
    answer.append(max(array))
    answer.append(n)
            
    return answer