######################## OOP in Python ########################

class pandas: # making class
    owner = "RK" #Class variable
    
    def __init__(self,name): #constructer
        self.name = name                #instance variable
        print("{0} in pnandas".format(name))

    def method(self): #method
        print('Method')
        
    def update(upname):
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
         self.lap = self.laptop()  # make class objector in construcor
         
         
    def show(self):
        print(self.name,self.rollno)
    
    class Laptop:
        
        def __init__(self):
                self.brand = "Asuss"
                self.cpu = "i7"
                self.ram = 8 
                
t1 = Student("Rohan",98123)
t2 = Student("Ravindi",98615)

lap1 = t1.lap
lap2 = t2.lap


          
          