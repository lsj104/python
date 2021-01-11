user = input("숫자를 입력해 주세요:")
num = user.split(",")
total = 0
for i in num:
    total += int(i)
print(total)
