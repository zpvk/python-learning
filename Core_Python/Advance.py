#Air Bus lording system in strach

class Flight():
    """IN this class contains all flight ditails for process
    """
    def __init__(self, color, p_capacity, l_storage):
        self.color = color
        self.p_capacity = p_capacity
        self.l_storage = l_storage
        self.passengers = []
    
    def add_pasenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.p_capacity - len(self.passengers)



flight = Flight("black",4,20)

people = ['Rohan',"ravinidi","Pasan","kavindu","Manel"]

for person in people:
    if flight.add_pasenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No avalable seat for {person}")

