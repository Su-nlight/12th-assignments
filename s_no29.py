
def mixedFraction(nume, deno):
    remainder=nume%deno
    quotient = int(nume / deno)
    if remainder!=0:
        res="{0}/{1} is equal to {2}({3}/{1})".format(nume, deno, quotient, remainder)
    elif quotient<0:
        res="Negative fractions not calculable"
    elif remainder==0:
        res="It is a proper fraction"
    return res

def main():
    try:
        nume=int(input("Enter the numerator: "))
        deno=input("Enter the denominator: ")
        if deno=="" or deno.isalpha() or deno.strip()=="0":
            print("value of the denominator assigned is invalid so assuming it as 1")
            deno=1
            x=mixedFraction(nume,deno)
        elif nume>int(deno) and int(deno)>0:
            x=mixedFraction(nume,int(deno))
        print(x)
    except ValueError:
        print("Numerator is invalid")


if __name__=="__main__":
    main()