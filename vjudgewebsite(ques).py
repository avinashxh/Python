#1
n = 1000
for i in range(1,n+1):
    print("Hello World")
#2
a,b  = map(int,input().split())
if(a<b):
    print("a < b")
if(a>b):
    print("a > b")
if(a==b):
    print("a == b")
#3
l,b = map(int,input().split())
area = l*b
print(area)
#4
a,b,c  = map(int,input().split())
if (a+b)>c and (a+c)>b and (b+c)>a :
    print("Yes")
else:
    print("No")
#5
n = int(input())
for i in range (1,101):
    i+=1
    print(i)
if(n!=i):
     print(n)
#6
a = int(input()) #students
b = int(input())  #apple they pick up
c = b%a
print(c)

#7
n = int(input())
s =0
while(n!=0):
    d = n%10
    s = s*10+d
    n = n//10
print(s)



