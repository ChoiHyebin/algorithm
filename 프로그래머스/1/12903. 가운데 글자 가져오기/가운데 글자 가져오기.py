def solution(s):
    res = ''
    length = len(s)
    mid = 0
    
    if length % 2 == 0:
        mid = length // 2
        res = s[mid-1:mid+1]
        return res
    else:
        mid = int(length // 2)
        res = s[mid]
        return res