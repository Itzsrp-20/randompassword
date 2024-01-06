#password generator
import random
letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num=['1','2','3','4','5','6','7','8','9','0']
spec=['!','@','#','$','%','^','&','*','?']
alp=int(input("enter the no of letter in your password\n"))
nu=int(input("enter the no of numbers in your password\n"))
spl=int(input("enter the no of special charecters in your password\n"))
tc=alp+nu+spl
password=''
newpassword=''
new_pass=[]
for i in range(0,alp):
    password=password+letter[random.randint(0,50)]
for j in range(0,nu):
    password=password+num[random.randint(0,9)]
for k in range(0,spl):
    password=password+spec[random.randint(0,8)]
password_list=[]
l=len(password)
for i1 in range(0,l):
    password_list.append(password[i1])
random.shuffle(password_list)
for i2 in range(0,l):
    newpassword=newpassword+password_list[i2]
print("Your generated password is ",newpassword)