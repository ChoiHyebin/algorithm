def solution(myString, pat):
    result = 0
    
    for i in range(len(myString)):
        if pat in myString[i:i+len(pat)]:
            result += 1
        
    return result