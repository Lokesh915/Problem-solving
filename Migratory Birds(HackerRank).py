def migratoryBirds(arr):
    x=len(arr)
    b=[0]*x
    for i in arr:
        b[i]=b[i]+1
    big=b.index(max(b))
    return big
