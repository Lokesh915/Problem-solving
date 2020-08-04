def breakingRecords(scores):
    H_scores=0
    L_scores=0
    max=scores[0]
    min=scores[0]
    for i in scores:
        if i>max:
            max=i
            H_scores+=1
        elif i<min:
            min=i
            L_scores+=1
    return [H_scores,L_scores]
