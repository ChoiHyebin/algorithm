def solution(num_list, n):
    answer = []
    tmp = []
    for i in num_list:
        tmp.append(i)
        if len(tmp) == n:
            answer.append(tmp)
            tmp = []
            
    return answer