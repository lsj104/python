#점프투파이썬 6장
class FourCal:
    def setdata(self, first, second):#메서드의 매개변수, 첫 번째 매개변수 이름은 self
        self.first = first  #메서드의 수행문
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = FourCal()
a.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())

