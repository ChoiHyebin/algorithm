def solution(rsp):
    answer = ''
    d = {'0':'5', '2':'0', '5':'2'}
    
    for i in rsp:
        answer += d.get(i)
        
    return answer