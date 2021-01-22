#점프투파이썬 6장
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):#메서드의 매개변수, 첫 번째 매개변수 이름은 self
        self.first = first  #메서드의 수행문
        self.second = second
    def div(self):
        result = self.first / self.second
        return result

#메서드 오버라이딩
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0: #나누는 값이 0인 경우 숫자 0을 돌려주도록 수정
            return 0
        else:
            return self.first / self.second
a = SafeFourCal(4, 0)
print(a.div())
