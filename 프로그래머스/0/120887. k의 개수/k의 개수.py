def solution(i, j, k):
    answer = 0
    li = []
    
    for w in range(i, j+1):
        li.append(str(w))
    
    k = str(k)
    
    for i in li:
        answer += i.count(k)

    return answer