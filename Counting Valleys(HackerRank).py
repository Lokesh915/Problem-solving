def countingValleys(n, s):
    sealevel=0
    counter=0
    for i in s:
        if i=='D':
            sealevel-=1
        if i=='U':
            sealevel+=1
        if sealevel==0 and i=='U':
            counter+=1
    return counter