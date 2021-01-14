eng = int(input("영어 점수입력:"))
math = int(input("수학 점수입력:"))

if eng + math > 110:
    if eng and math >40:
        print("합격입니다")
    else:
        print("불합격입니다")
else:
    print("불합격입니다")
