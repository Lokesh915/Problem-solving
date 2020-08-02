def compareTriplets(a, b):
    e=0
    f=0
    
    for i in range(0,len(a)):
        if a[i]>b[i]:
            e+=1
        
        elif a[i]<b[i]:
            f+=1
        
    return [e,f]