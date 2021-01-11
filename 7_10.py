class Calculator:
    def __init__(self, numberlist):
        self.numberlist = numberlist

    def add(self):
        result = 0
        for num in self.numberlist:
            result += num
        return result

    def avg(self):
        total = self.add()
        return total / len(self.numberlist)

cal1 = Calculator([1,2,3,4,5])
print("1,2,3,4,5의 합계와 평균은")
print(cal1.add())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print("6,7,8,9,10의 합계와 평균은")
print(cal2.add())
print(cal2.avg())
