######################## OOP in Python ########################

class pandas: # making class
    owner = "RK" #Class variable
    
    def __init__(self,name): #constructer
        self.name = name                #instance variable
        print("{0} in pnandas".format(name))

    def method(self): #method
        print('Method')
        
    def update(self,upname):
        pandas.owner=upname
        print(pandas.owner)
    
    def book(self,Name,date):
        self.Name = Name
        self.date = date
        
        print(self.Name,self.date)
        
pnd = pandas("Rohan") #making object using class
pnd2 = pandas("Ravindi")

pnd.method()

#update class variable
pandas.update("HMRK")

#Addrass of the object

print(id(pnd))

#Memory size calculate by constructer

pnd.book("Madolduwa",90-78)
pnd2.book("hinsare",56-89) 

class Student:
    
    School = "NSBM"
    
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
   
    def get_m1(self): #getter 
        return self.m1
    
    def set_m1(self,value): #setter
        self.ml = value
    
    @classmethod         # cls and this line use for class method
    def info(cls):
        return cls.School
    
    @staticmethod 
    def infocls():
        print("This is Student class")
            

            
s1 = Student(89,56,56)
s2 = Student(45,89,75)

print(s1.avg())
print(s2.avg())

print(Student.info())
Student.infocls()

######### class in class ##########3

class Student1:
    def __init__(self,name,rollno):
         self.name = name
         self.rollno = rollno
         self.lap = self.Laptop()  # make class objector in construcor
         
         
    def show(self):
        print(self.name,self.rollno)
    
    class Laptop:
        
        def __init__(self):
                self.brand = "Asuss"
                self.cpu = "i7"
                self.ram = 8 
                
t1 = Student1("Rohan",98123)
t2 = Student1("Ravindi",98615)

lap1 = t1.lap
lap2 = t2.lap


#inheritance in python

class A:  #1st class(Super class)
    def __init__(self):
        print("A init")
    def method1(self):
        print("This is method 1")
    def method2(self):
        print("This is method 2")
    def method3(self):
        print("This is method 3")
    def methodd(self):
            print("This is class D but in A")

#singal class inheritance
#one super class & one sub class
# for inharite class we use with in () we use class name tharefor we can inharite uper class from down class 
class B(A): # 2nd class
    def method4(self):
        print("This is method 4")
    def method5(self):
        print("This is method 5")
    def method6(self):
        print("This is method 6")

#now we can use uper class method form class B object

obj1 = B()
obj1.method1()

#multi level inharitance
#one supper class and 2 sub class
class C(B):  #3rd class(Super class)
    def __init__(self):
        print("class C constructr")
    
    def method7(self):
        print("This is method 7")
    def method8(self):
        print("This is method 8")
    def method9(self):
        print("This is method 9")
        
obj2 = C()
obj2.method2()

#multipule inheritance you can use more class in this method like this

class D:
    def __init__(self):
        print("This is class D constructer")
    
    def methodd(self):
        print("This is class D")
        
        
class F:
    def __init__(self):
        print("This is class F constructrer")
        
    def methodf(self):
        print("this is clss F")
        
class I(C,D,F): # multiple inharitance use like this
    def __init__(self):
        super().__init__() # hear i call class supper class constructor but hear, have 3 supper class what int can be call?
        print("in F in init")
    # it's call from left to right
    #fristly call constructor in c then call D
    #it's called Method Resolution Order(MRO)
    

obji = I()


