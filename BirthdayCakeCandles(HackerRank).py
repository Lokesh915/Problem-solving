def birthdayCakeCandles(ar):
    large=ar[0]
    l_candels=0
    for i in ar:
        if i>=large:
            l_candels+=1
    return l_candels

