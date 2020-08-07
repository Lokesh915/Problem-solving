def bonAppetit(bill, k, b):
    bill.remove(bill[k])
    b_actual=sum(bill)
    b_actual=b_actual//2
    
    if b==b_actual:
        print( "Bon Appetit")
    else:
        final= b-b_actual
        print( final) 