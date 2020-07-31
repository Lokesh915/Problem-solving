def timeConversion(s):
    
    if s[:2] == '12' and s[-2] == 'A':
        return '00'+s[2:8]
    elif s[:2] == '12' and s[-2] =='P' or s[-2] == 'A':
        return s[:8]
    else:
        k = int(s[:2]) + 12
        return str(k)+s[2:8]