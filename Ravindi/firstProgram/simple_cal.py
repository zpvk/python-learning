#simple 2 digit calculator
num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2st number: "))
sum = num1+num2
sub = num1-num2
mult = num1*num2
div = num1/num2
fldiv = num1//num2
mod = num1%num2
round = round(num1)
absoulte = abs(num1)

print("\n{} + {} = {}".format(num1,num2,sum))
print("{} - {} = {}".format(num1,num2,sub))
print("{} * {} = {}".format(num1,num2,mult))
print("{} / {} = {}".format(num1,num2,div))
print("{} // {} = {}".format(num1,num2,fldiv))
print("{} % {} = {}\n".format(num1,num2,mod))