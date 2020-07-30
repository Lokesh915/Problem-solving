def miniMaxSum(arr): #by looping
    min=arr[0]
    max=arr[0]
    sum=0
    for i in arr:
        if i<min:
            min=i
        elif i>max:
            max=i
    for i in :
        sum=sum+i
    print(sum-max,sum-min)

def miniMaxSum(arr):  #inbilt functions

    small=min(arr)
    big=max(arr)

    print(sum(arr)-big,sum(arr)-small)

