def solution(s):
    res = []
    d = {}
    
    for i in range(len(s)):
        if s[i] not in d:
            res.append(-1)
        else:
            res.append(i - d[s[i]])
        d[s[i]] = i
        
    return res