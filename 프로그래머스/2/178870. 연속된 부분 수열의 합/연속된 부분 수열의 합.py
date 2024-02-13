def solution(sequence, k):
    answer = []
    sum = 0
    h = 0
    t = -1
    
    while True:
        if(sum < k):
            t += 1
            if(t >= len(sequence)):
                break
            sum += sequence[t]
        else:
            sum -= sequence[h]
            if(h >= len(sequence)):
                break
            h += 1
        if(sum == k):
            answer.append([h, t])
        
    answer.sort(key = lambda x : (x[1]-x[0], x[0]))
        
        
    return answer[0]