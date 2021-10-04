'''n1,n2=0,1
number=int(input("enter the number:"))
count=0
if number<0:
    print("please enter +ve number")
elif number==1:
    print(n1)
else:
    while count<number:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
number=int(input("enter the number:"))
fact=1
if number<0:
    print("please enter the +ve number")
elif number==0:
    print(fact)
else:
    for i in range(1,number+1):
        fact*=i
print(fact)

str1=input("enter the string")
if str1==str1[::-1]:
    print("pal")
else:
    print("not a pal")
number=int(input("enter the number:"))
flag=False
if number>2:
    for i in range(2,number):
        if number%i==0:
            flag=True
            break
if flag:
    print("not a prime")
else:
    print("prime")
number=int(input("enter the number:"))
if number%2==0:
    print("even number")
else:
    print("odd number")'''


class Prism():
    def extract(scpu,ram):
        print("extraction")
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("initialing")

obj=Prism("i5",4)
Prism.extract("i5",4)

