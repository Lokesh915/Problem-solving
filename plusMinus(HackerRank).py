def plusMinus(s):

    positive=0
    negative=0
    zero=0

    for i in s:
       
        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        elif i==0:
            zero+=1
    print(positive/len(s))
    print(negative/len(s))
    print(zero/len(s))
    
    
plusMinus([1,2,-1,-3,0,0])
