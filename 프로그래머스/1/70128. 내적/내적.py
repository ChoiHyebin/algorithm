def solution(a, b):
    result = 0
    arr = []
    
    for i in range(len(a)):
        arr.append(a[i]*b[i])
    
    result = sum(arr)
    
    return result