weight = int(input("몸무게를 입력해 주세요:"))
height = int(input("키를 입력해 주세요:"))
height/=100

bmi = weight/(height*height)

if bmi<20:
    print("저체중")
elif bmi >= 20 and bmi <= 24:
    print("정상체중")
elif bmi >= 25 and bmi <= 30:
    print("경도비만")
else:
    print("비만")
    
