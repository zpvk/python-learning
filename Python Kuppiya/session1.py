# # # this code for the Inputs
# name = str(input("Enter Your Name : "))
# age = str(input("Enter Your Age : "))
# address = str(input("Enter Your Address : "))
# batch = str(input("Enter Your Batch : "))
# mobile = str(input("Enter Your Mobile Number : "))
# vilage = str(input("Enter Your Village Name : "))

# # # this code for the bio
# print("\n{x} This is your Bio {x}\n".format(x = "*"*10))
# print("Name : {}\nAge : {}\nAddress : {}\nBatch :{}\nMobile Number : {}\nVillage : {}\n\n{}"
# .format(name,age,address,batch,mobile,vilage,"*"*38))

# num1 = int(input("Enter 1st number: "))
# num2 = int(input("Enter 2st number: "))
# sum = num1+num2
# sub = num1-num2
# mult = num1*num2
# div = num1/num2
# fldiv = num1//num2
# mod = num1%num2
# print("\n{} + {} = {}".format(num1,num2,sum))
# print("{} - {} = {}".format(num1,num2,sub))
# print("{} * {} = {}".format(num1,num2,mult))
# print("{} / {} = {}".format(num1,num2,div))
# print("{} // {} = {}".format(num1,num2,fldiv))
# print("{} % {} = {}\n".format(num1,num2,mod))
# num1 = int(input("Enter 1 Number"))
# num2 = int(input("Enter 2 Number"))

# print(num1 + num2)
# print (num1 - num2)

# x = 5
# y = 10

# if(y==x):
#     print("Yes")
# else:
#     print("No")

# if(y==x):
#     print("Yes")
# elif(y>x):
#     print("ok")
# else:
#     print("No")

# print("{x} Welcome to my Calculator {x}\n".format(x="*"*10))
# num1 = int(input("Enter Your 1st Number : "))
# print("\n  Add + \n  Subtract - \n  Multiple * \n  Divide / \n  Exponet ** \n  Mod % \n  Div //\n")
# oprator = str(input("Enter Your Oparator : "))
# num2 = int(input("Enter Your 2nd Number : "))

# if(oprator == "Add" or oprator == "+"):
#     print("Answer : ",num1+num2)
# elif(oprator == "Subtract" or oprator == "-"):
#     print("Answer : ",num1-num2)
# elif(oprator == "Multiple" or oprator == "*"):
#     print("Answer : ",num1*num2)
# elif(oprator == "Divide" or oprator == "/"):
#     print("Answer : ",num1/num2)
# elif(oprator == "Exponet" or oprator == "**"):
#     print("Answer : ",num1**num2)
# elif(oprator == "Mode" or oprator == "%"):
#     print("Answer : ",num1%num2)
# elif(oprator == "Div" or oprator == "//"):
#     print("Answer : ",num1//num2)
# else:
#     print("Your oprator is invalid :( Please try again")



# num1 = int(input("Enter 1 Number"))
# print("sum/n sub/n""multi/n""dvi/n""tdvi/n""sdvi/n")
# x=str(input("Enter Your opertor"))
# num2 = int(input("Enter 2 Number"))
# if(x=="sum"):
#     print(num1+num2)
# elif(x=="sub"):
#     print(num1-num2)
# elif(x=="multi"):
#     print(num1*num2)
# elif(x=="dvi"):
#     print(num1/num2)
# elif(x=="tdvi"):
#     print(num1//num2)
# elif(x=="sdvi"):
#     print(num1%num2)
# else:
#     print("Plaase Try Again")   



#Define funtion (adds two numbers)
# def add(x,y):
#     return x + y
# #Define funtion (subtracts two numbers)
# def subtract(x,y):
#     return x - y
# #Define funtion (multiples two numbers)
# def multiple(x,y):
#     return x * y
# #Define funtion (devides two numbers)
# def devided(x,y):
#     return x / y
# print("select operations.")
# print("1.add")
# print("2.subtract")
# print("3.multiple")
# print("4.devide")
# choice=input("Enter choice(1/2/3/4: ")
# Num1=float(input("Enter first number: "))
# Num2=float(input("Enter second number: "))

# if choice=='1' :
# print(num1,"+",num2,"=",add(num1,num2))
# else if choice=='2' :
# print(num1,"+",num2,"=",subtract(num1,num2))
# else if choice=='3' :
# print(num1,"+",num2,"=",multiple(num1,num2))
# else if choice=='4' :
# print(num1,"+",num2,"=",devide(num1,num2))
# else:
# print("invalid input")

# x = int(input("Enter 1st no: "))
# print("1 - Add\n2 - Substract\n3 - Multiply\n4 - Divide\nSelect perefered operetor by number")
# opp = int(input("Enter your option: "))
# y = int(input("Enter 2nd no: "))
# if(opp == 1):
#     print("{} + {} =".format(x,y),x+y)
# elif(opp == 2): 
#     print("{} - {} =".format(x,y),x-y)
# elif(opp == 3): 
#     print("{} * {} =".format(x,y),x*y)
# elif(opp == 4): 
#     print("{} - {} =".format(x,y),x/y)
# else:
#     print("something went wrong. Try Again")

print("{x} Pass Mark Genarator {x}\n".format(x="*"*20))
score = int(input("Enter your Score : "))
mark = "Undifine"
if (score>= 0 or score<=100 ):
    if(score < 35):
        mark = "Fail"
    elif(score <= 35 or score<= 44):
        mark = "S"
    elif(score <= 45 or score<= 64):
        mark = "C"
    elif(score <= 65 or score<= 74):
        mark = "B"
    elif(score <= 75 or score<= 94):
        mark = "A"
    elif(score <= 95 or score<= 100):
        mark = "A+"
    

print("Your Pass Mark is : ",mark)
print("\n{x}".format(x="*"*61))




