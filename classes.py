#encoding = 'utf-8'

class Summation:


    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.list_ = []


    def summ(self):
        return self.a + self.b

    def cr_dict(self):
        self.list_.append([self.a, self.b])
        return self.list_

    def return_list(self):
        print(self.list_)


s = Summation(4, 5)
k = Summation.summ(s)
print(k)