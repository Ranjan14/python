def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2,n):
            c=a+b
            print(c,end=" ")
            a=b
            b=c


n=int(input("Enter the number"))
fib(n)
