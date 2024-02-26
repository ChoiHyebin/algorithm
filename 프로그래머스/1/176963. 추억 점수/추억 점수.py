def solution(name, yearning, photo):
    res = []
    dic = dict(zip(name, yearning))
    
    for people in photo:
        score = 0
        for person in people:
            score += dic.get(person, 0) # 없는 사람은 0
        res.append(score)
    
    return res