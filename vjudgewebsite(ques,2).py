w = int(input())
l =[]
if w%2==0 :
    print("YES")
    for i in range(2,w//2+1,2):
        l.append([i,w-i])
    print(l)

