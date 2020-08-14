def getMoneySpent(keyboards, drives, b):
    min_keyboard=min(keyboards)
    min_drives=min(drives)
    if min_keyboard+min_drives>b:
        return(-1)
    count=[]
    sum=0
    for i in keyboards:
        for j in drives:
            sum=i+j
            if sum<=b:
                count.append(sum)
    return max(count)