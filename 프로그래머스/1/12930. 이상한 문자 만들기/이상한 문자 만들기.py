def solution(s):
    arr = []
    arr = s.split(" ")
    
    res = ""
    
    for i in arr:
        for j in range(len(i)):
            if j%2 == 0:
                res += i[j].upper()
            else:
                res += i[j].lower()
        res += " "
    
    return res[0:-1]