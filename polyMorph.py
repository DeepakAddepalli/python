import genrator_eg
class Car:
    def __init__(self, seats, regno=None):
        self.seats = seats
        self.regno = regno

    def __str__(self):
        return "I am {} seater car".format(self.seats)

    def __len__(self):
        return self.seats

    def __repr__(self):
        return "seats ={}, registered={}".format(self.seats,self.regno)

    def __add__(self, other):
        return self.seats + other.seats

    def __bool__(self):
        if self.regno:
            return True
        else:
            return False

    def __del__(self):
        print("bye,bye")


zen = Car(5)
innova = Car(8, "AP28 4892")

print(zen)
print(len(zen))
if zen:
    print(zen, "I am registered")
if innova:
    print(innova, "I am registered")

#del zen

print(repr(innova))
print(zen + innova)

for x in genrator_eg.Squares(30):
    print(x)

    x =(x*x for x in range(30)) ##generator

for y in x:
    print(y)