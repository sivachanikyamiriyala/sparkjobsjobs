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
    print("odd number")


class Prism():
    def extract(scpu,ram):
        print("extraction")
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("initialing")

obj=Prism("i5",4)
Prism.extract("i5",4)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
=======
>>>>>>> ba3091a (4th commit)
=======
>>>>>>> remotes/origin/master
def hello():
    print("allprogg")
def hello1():
    print("hello1")
import logging
logging.basicConfig(filename='c:\\Users\DELL\PycharmProjects\sivaProject\main.py',level=logging.INFO)
logging.info("initialing")
<<<<<<< HEAD

print(__name__)
'''
def extraction(x):
    '''
    :param x:string

    :param x:
    :return: maskedmail in string format
    '''
    l1=len(x)
    mail=x.split("@")[0]
    list_mail=list(mail)
    list_mail[1:int(l1)-1]="x"*(int)(l1-2)
    return "".join(list_mail)+"@"+x.split("@")[1]
<<<<<<< HEAD
>>>>>>> 4488695 (5th commit)
=======
>>>>>>> remotes/origin/master
=======
'''
print(__name__)
>>>>>>> ba3091a (4th commit)
