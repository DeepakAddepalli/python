class Car:
    def __init__(self,seats,regno):
        self.seats=seats
        self.regno=regno
    def __hash__(self):
        return hash(self.regno)

zen=Car(5,"TS29 2842")
print(hash(zen))
ritz=Car(5,"TS30 2232")
print(hash(ritz))
