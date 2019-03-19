class Dog:
    def __init__(self,color,breed):
        self.color=color
        self.breed=breed
    def run(self):
        print("deepak runs faster than me")

    def bark(self):
        print("bow...bow")

oliver= Dog("brown","lab")

print(type(oliver))
print(isinstance(oliver,Dog))
oliver.run()
oliver.bark()
