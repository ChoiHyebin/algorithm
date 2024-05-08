def solution(array):
    answer = 0
    
    n = len(array)
    m = int(n/2)
    
    array = sorted(array)
    answer = array[m]
    
    return answer