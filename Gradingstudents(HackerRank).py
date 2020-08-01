   count=[]
    for i in grades:
        if i>=38 and i%5>=3:
            i=i+(5-i%5)
            count.append(i)
        else:
            count.append(i)
    return count