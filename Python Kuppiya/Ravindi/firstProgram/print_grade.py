# home work 3
# print the grade when student enter his marks

print("{x} Grade Calculator {x}\n".format(x="*"*10))

marks = int(input("Enter your module mark : "))

if(marks>=0 and marks<=100):
    print("Hello Student\n")
    if(marks>=75):
        print("Fabulous! Your grade is A")
    elif(marks>=65):
        print("Awesome! Your grade is B")
    elif(marks>=55):
        print("Great!, Your grade is C")
    elif(marks>=45):
        print("Nice! Your grade is D")
    elif(marks<35):
        print("Oh! Your grade is F. Work harder")
else:
    print("invalid input")

print("\n{x} Have a good day {x}".format(x="*"*10))

