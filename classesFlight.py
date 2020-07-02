class Flight():
    def __init__(self , capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self , name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)

people = ["Harry" , "Harmione" ,"Ron" , "Ginny"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight succesfully !!")
    else:
        print(f"No available seats for {person}")


#Output
# Added Harry to flight succesfully !!
# Added Harmione to flight succesfully !!
# Added Ron to flight succesfully !!
# No available seats for Ginny
