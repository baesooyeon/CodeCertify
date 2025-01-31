def solution(elements):
    new_elements = 2*elements
    l = len(elements)

    history = [0]*1000001
    answers = 0
    for i in range(1, l+1):
        for j in range(l):
            x = sum(new_elements[j:j+i])
            if history[x]==0:
                history[x]=1
                answers+=1
    return answers