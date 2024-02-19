#enter a number and check if it is prime and even or not
# num = int(input("enter :"))
# count = 0
# if num % 2 == 0:
#     print(num, "is even")
# else:
#     print(num, "is not even")
# for i in range (1,num+1):
#     if (num%i==0):
#         count+=1
# if(num%i==0) and (count==2):
#          print("prime")
# else :
#     print("not prime")

#is it raining or snowing (true if either is true)

def getData(weather):
    return input(f"is it {weather}").lower()
def checking(data) :
    while not(data == "yes" or data == "no") :
        return data
rain = checking(getData("Raining"))
snow = checking(getData("Snowing"))











