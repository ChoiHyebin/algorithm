def solution(arr1, arr2):
    res = []
    
    for i in range(len(arr1)):
        total = []
        for j in range(len(arr1[0])):
            total.append(arr1[i][j] + arr2[i][j])
        res.append(total)
    
    return res
    