def solution(s):
    li = list(s.split(" "))
    n = list(map(int, li))
    
    max_num = max(n)
    min_num = min(n)
    
    s = ""
    s = str(min_num) + " " + str(max_num)
    
    return s