# home work 2 (calculator)
# 01) input first digit
# 02) show operators have
# 02) input operator need
# 03) input 2nd digit
# 04) show answer

x = int(input("Enter 1st no: "))
print("1 - Add\n2 - Substract\n3 - Multiply\n4 - Divide\nSelect perefered operetor by number")
opp = int(input("Enter your option: "))

y = int(input("Enter 2nd no: "))

if(opp == 1):
    print("{} + {} =".format(x,y),x+y)
elif(opp == 2): 
    print("{} - {} =".format(x,y),x-y)
elif(opp == 3): 
    print("{} * {} =".format(x,y),x*y)
elif(opp == 4): 
    print("{} - {} =".format(x,y),x/y)
else: 
    print("something went wrong. Try Again")



#need to find the error
# this is wrong
# need to run a loop in fisrt if 
x = int(input("Enter 1st no: "))
print("1 - Add\n2 - Substract\n3 - Multiply\n4 - Divide\nSelect perefered operetor by number")
opp = int(input("Enter your option: "))

if(opp != 1 | opp != 2 | opp != 3 | opp != 4 ):
    print("Check the opertor no and try again")
    opp = int(input("Enter your option: "))
else:
    y = int(input("Enter 2nd no: "))

if(opp == 1):
    print("{} + {} =".format(x,y),x+y)
elif(opp == 2): 
    print("{} - {} =".format(x,y),x-y)
elif(opp == 3): 
    print("{} * {} =".format(x,y),x*y)
elif(opp == 4): 
    print("{} - {} =".format(x,y),x/y)
else: 
    print("something went wrong. Try Again")

