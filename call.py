class Converter:
    def __init__(self,multiple):
        self.multiple=multiple
    def __call__(self,n):
        return n*self.multiple

mm2cm=Converter(1/10)
mtr2mm=Converter(1000)
mile2km=Converter(1.6)

print(mile2km(10))
print(mm2cm(1))
print(mtr2mm(2))