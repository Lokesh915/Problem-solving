def divisibleSumPairs(n, k, ar):
    
    count=0
    for i in range(len(ar)):
        for j in range(len(ar)):
            sum=0
            if i<j:
                sum=ar[i]+ar[j]
                if sum%k==0:
                    count+=1           
    return count