def solution(seoul):
    res = ""
    num = 0
    
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            num = i
            res = "김서방은 " + str(i) + "에 있다"
    
    return res