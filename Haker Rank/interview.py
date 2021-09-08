# list1 = ["A","B","C","A"]
# set1 = {"A","B","C","A"}
# print(set1)
# print(list1)

# for i in range(0,6):
#     print("*"*(5-i))

x =[1,2,3,4,5,5]
print("Avrage :",sum(x)/len(x))
mid = len(x)/2

def median(x):
    lenth = len(x)
    if lenth%2 == 0:
        mid = round(len(x)/2)
        summ = (x[mid]+x[mid-1])/2
        print("median :", summ)
    else:
        mid = round(len(x)/2)
        print("median :", x[mid-1])
median(x)

def mode(x):
    y = {}
    for i in x:
        y = {i:x.count(i)}
    
    print("Mode : ", max(y))
mode(x)