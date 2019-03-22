class Squares:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        output = self.count ** 2
        self.count += 1
        if self.count <= self.n:
            return output
        else:
            raise StopIteration

def main():
    for number, square in enumerate(Squares(30)):
        print(number, square)

    j = Squares(1000000000)
    print(type(j))
    import sys

    print(sys.getsizeof(j))

if __name__ =="__main__":
    main()










