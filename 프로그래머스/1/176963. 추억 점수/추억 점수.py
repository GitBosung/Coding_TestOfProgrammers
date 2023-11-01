def solution(name, yearning, photo):
    namescore = dict(zip(name, yearning))
    answer = []
    
    for i in photo:
        total = 0
        for inname in i:
            score = namescore.get(inname, 0)
            total += score
        answer.append(total)
            
    return answer