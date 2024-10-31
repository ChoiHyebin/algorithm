def solution(emergency):
    answer = []
    
    e_sort = sorted(emergency)
    e_sort.reverse()
    
    print(e_sort)
    for i in emergency:
        answer.append(e_sort.index(i)+1)
        
    return answer