def solution(array, n):
    answer = 0
    min_num = []
    
    array.sort()
    for i in array:
        min_num.append(abs(i-n))
    
    minimum = 0
    minimum = min(min_num)
    
    idx = []
    idx.append(min_num.index(minimum))
    
    answer_idx = min(idx)
    answer = array[answer_idx]
    
    return answer