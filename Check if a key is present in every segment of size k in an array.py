# Check if a key is present in every segment of size k in an array 

ar=[5, 8, 9, 12, 14, 9, 9]
k=3
f=9
def key_in_every_segment(ar,k,f):
    i=0 #initialisation for slicing i is start point
    j=k #initialisation for slicing j is end point
    x=[] # for adding segments
    count=0
    while j<=len(ar):
        x.append(ar[i:j]) #sclicing segments and adding to array x
        i+=k # incrementing i for sclicing next segment 
        j+=k 
    # if array is in odd size with respect to given k then it sclices odd part and adds to array x   
    if len(ar)%k!=0: 
        s=len(ar)%k
        x.append(ar[-s:])
    #for checking wheter f present in every segment
    for i in x:
        if f in i:
            count+=1
    #if f is present in every segment then count should equals to length of x
    if count==len(x):
        print('Yes')
    else:print('No')
    
key_in_every_segment(ar,k,f)