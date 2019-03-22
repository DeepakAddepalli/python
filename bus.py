class Bus(object):
    def __init__(self, driver):
        self.driver = driver
    def __getattr__(self, item):
        print("sorry we didn;t find {}".format(item))


a = Bus('Ravi')
print(a.driver)
print(a.conductor)
print(a.reg_no)
