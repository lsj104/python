import random
n = random.randint(1, 50)
print("1부터 50사이의 숫자를 맞추세요")
while True:
    m = int(input("숫자를 입력하세요:"))
    if m < n :
        print("높습니다")
        continue
    elif m > n :
        print("낮습니다")
        continue
    else:
        print("축하합니다")
        break

        
