def birthday(s, d, m):
    
    count=0
    
    for i in range(len(s)):
        total=0
        total=total+sum(s[i:i+m])
        if total==d:
            count+=1
        
    return count
