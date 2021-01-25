import tkinter #GUI모듈 포함시키기
from math import*
window=tkinter.Tk() #가장 상위 레벨의 윈도우 창 생성
window.title("EX_4") #윈도우 창의 제목설정
window.geometry("640x400+100+100") #너비x높이+x좌표+y좌표
window.resizable(False,False) #창 크기 조절 가능여부 ,True로 설정할 경우 크기조절가능

def calc(event):
    label.config(text="결과="+str(eval(entry.get())))

entry = tkinter.Entry(window) #기입창의 속성 설정
entry.bind("<Return>", calc) #메소드나 함수 실행
entry.pack()

label=tkinter.Label(window)
label.pack() #위젯 배치, 기본속성=최상단
window.mainloop() #윈도우 창을 윈도우가 종료될 때 까지 실행