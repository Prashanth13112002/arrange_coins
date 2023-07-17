def arrange(n):
    
    i = 1
    c = 0
    while(n>0):
        
        n -= i
        c += 1
        if (n < 0):
            
            c -= 1
        
            return c
        elif n == 0:
            
            return c
            
        i += 1

n = int(input())        
print(arrange(n))