#If-else statements
a=int(input("Enter your age"))
print("Your age is :" ,a)
if(a>18):
    print("You can drive and if you drive please drive safely")
else:
    print("You cannot drive because your age is not 18 ")


#elif statements
num=0
if(num>0):
    print("Number is negative")
elif(num==0):
    print("Number is zero")
else:
    print("Number is positive")

#Nested-if statementss
num=18
if(num<0):
    print("Number is negative")
elif(num>0):
    if(num<=10):
        print("numbe ris between 11-20")
    else:
        print("number is zerooo")