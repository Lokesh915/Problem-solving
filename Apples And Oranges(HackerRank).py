def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple=[]
    orange=[]
    count=0
    count1=0

    for i in apples:
        i=i+a
        apple.append(i)
    for i in oranges:
        i=i+b
        orange.append(i)
    for i in apple:
        if i>=s and i<=t:
            count+=1
    for i in orange:
        if i >=s and i<=t:
            count1+=1
    print(count)
    print(count1)