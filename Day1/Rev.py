def rev(n):
    if n<0:
        flag=1;
        n= n*(-1)
    a = n
    ans=0
    while a>0:
        ans = (ans*10)+ (a%10)
        a = a//10
    if(flag==1):
        ans = ans *(-1)
    print(ans)
#reverse of given number
rev(456) # n=456 # n = int(input())