def rev(n):
    a = n
    ans=0
    while a>0:
        ans = (ans*10)+ (a%10)
        a = a//10
    print(ans)
#reverse of given number
rev(456) # n=456 # n = int(input())