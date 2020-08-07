def sockMerchant(n, ar):
    sum=0
    socks=set(ar)
    for i in socks:
        sum=sum+ar.count(i)//2
        
    return sum