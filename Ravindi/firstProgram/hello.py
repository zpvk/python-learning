#This is my very first python program
# 'print' method use to show the message 
print("Hello Ravindi\nWelcome to Python Programming\n")

# assign values for variables and print them seperatly try this
x = 1
a, b, c = "Ravindi", "Rohan", "Apple"

print(a)
print(b)
print(c)


#try a simple for loop 
# for the String value "Ravindi" all the letters print in the console from one by one downwards
for x in "Ravindi" : 
    print (x)

# to retrieve the data type of the variable try out the following method called 'type'
a = 1
print(type(a))

#if you need to print two or more variables in one line follow this method
name = "Ravindi"
age = 23
print ("My name is {} and i'm {} old".format(name,age))


#taking data from outside
name = str(input("What's your name?"))
print(name)


#simple addition calculator
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
answer = num1+num2
print(answer)


#print same thing alone a line
print("\n{x}star{x}\n".format(x="*"*10))

# if only one variable is integrated with the line can keep the curly braces empty
print("\n{}star{}\n".format(x="*"*10, x="*"*10))