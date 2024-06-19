def solution(num_list):
    answer = []
    
    ans_len = len(num_list)
    
    for i in range(ans_len):
        answer.append(num_list[i])
    
    if num_list[ans_len-1] > num_list[ans_len-2]:
        answer.append(num_list[ans_len-1] - num_list[ans_len-2])
    else:
        answer.append(num_list[ans_len-1] * 2)
            
    return answer