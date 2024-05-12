def solution(n, k):
    answer = 0
    cnt = 0
    
    for i in range(1, n+1):
        if i%10 == 0:
            cnt += 1
    
    k = k - cnt
        
    answer = n*12000 + k*2000
    
    return answer