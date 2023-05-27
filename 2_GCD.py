def gcd(m,n):
    
    fac = []
    for i in range(1, min(m,n)+1):
        if m%i == 0 and n%i == 0:
            fac.append(i)
            
    print("Common factors of ",m," and ",n," is ",fac)
    print("GCD of ",m," and ",n," is ",fac[-1])
    
gcd(42936,5421)
gcd(1234567,321234)