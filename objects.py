class PartyAnimal:
    x = 0

    ##this one runs while stating of the class
    def __init__(self):
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    
    ## This methods runs end of the class 
    def __del__(self):
        print('I am destructed',self.x)

an = PartyAnimal()
an.party()
an.party()
an.party()
an.party()