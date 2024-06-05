from Firstdemo import Calculator

class ChildImp(Calculator):
    num2 = 200

    def __init__(self):                  # Child class constructor
        Calculator.__init__(self, 1, 3)  # parent class constructor calls in child class constructor

    def get_Complete_data(self):
        return self.num + self.num2 + self.Sum()


obj = ChildImp()
print(obj.num2)
print(obj.get_Complete_data())


