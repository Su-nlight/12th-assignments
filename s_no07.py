# Ans.i) ---------------------------------------------------------
def sum1series(n):
    total=0
    for i in range(1,(2*n)+1,2):
        total+=i
    return total

# Ans.ii) ---------------------------------------------------------
def sum2series(x,n):
    total=0
    for i in range(2,n+1):
        print(i)
        total+=(i/(x**(i-1)))
    return total

# Ans.iii) ---------------------------------------------------------
def factorial(x):
    fac=1
    for i in range(2,x+1):
        fac*=i
    return fac

def sum3series(n):
    total=0
    for i in range(1,n+1):
        total+=(i/factorial(i))
    return total
