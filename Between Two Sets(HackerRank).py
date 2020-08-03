def getTotalX(a, b):

    x=max(a)
    y=min(b)

    f_list=[]
    s_list=[]

    for i in range(x,y+1):
        count=0
        for j in a:
            if i%j==0:
                count+=1
            if count==len(a):
                f_list.append(i)
    for i in f_list:
        count1=0
        for j in b:
            if j%i==0:
                count1+=1
            if count1==len(b):
                s_list.append(i)
    return len(s_list)
