import tkinter #GUI모듈 포함시키기
window=tkinter.Tk() #가장 상위 레벨의 윈도우 창 생성

window.title("EX_3") #윈도우 창의 제목설정
window.geometry("640x400+100+100") #너비x높이+x좌표+y좌표
window.resizable(False,False) #창 크기 조절 가능여부 ,True로 설정할 경우 크기조절가능

count = 0

def countUP():
    global count
    count +=1
    label.config(text=str(count))

label=tkinter.Label(window,text="0")
label.pack() #위젯 배치, 기본속성=최상단

button = tkinter.Button(window, overrelief="solid", width = 15, command = countUP, repeatdelay=1000, repeatinterval=100)
button.pack()
window.mainloop() #윈도우 창을 윈도우가 종료될 때 까지 실행