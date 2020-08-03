def kangaroo(x1, v1, x2, v2):
    
    if v1<v2 and x1<x2:
        return('NO')
    elif v1==v2 and x2>x1:
        return('NO')
    else:
        while (x2>x1):
            x1+=v1
            x2+=v2

            if x1==x2:
                return ('YES')

            if x1>x2:
                return ('NO')
        