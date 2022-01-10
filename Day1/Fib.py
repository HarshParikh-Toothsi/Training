def fib(n):
    a,b = 0,1
    limit = n
    while limit > 0 :
        print(a)
        limit = limit-1
        a,b = b,a+b
#first n number of fibonacci series
fib(10) #n=10