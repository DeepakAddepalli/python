from math import factorial as fact

class Book:

    def __call__(self, n):
        return fact(n)

    def __init__(self):
        self.pages=["page1","page2","page3","page4","page5","page6",]
    def __iter__(self):
        self.count=0
        return self
    def __next__(self):
        if self.count<len(self.pages):
            output = self.pages[self.count]
            self.count += 1
            return output
        else:
            raise StopIteration

    def getnthpage(self,n):
        print(self.pages[n-1])
    def getallpages(self):
        print(self.pages)

mybook=Book()
mybook.getnthpage(3)
mybook.getallpages()

for page in mybook:
    print(page)

print(callable(mybook))
print(mybook(5))












