def diagonalDifference(n,arr):
    sum=0
    sum1=0
    i=0
    while i!=n:
        sum=sum+arr[i][i]
        sum1=sum1+arr[i][n-1-i]
        i+=1
    result=abs(sum-sum1)
    return result