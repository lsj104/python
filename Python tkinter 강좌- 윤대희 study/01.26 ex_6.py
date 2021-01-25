import tkinter

window=tkinter.Tk()
window.title("EX_6")
window.geometry("640x400+100+100")
window.resizable(False,False)

def flash():
    checkbutton1.flash()

CheckVariety_1 = tkinter.IntVar()
CheckVariety_2 = tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=CheckVariety_1, activebackground="blue")
checkbutton2=tkinter.Checkbutton(window, text="△", variable=CheckVariety_2)
checkbutton3=tkinter.Checkbutton(window, text="X", variable=CheckVariety_2, command=flash) #flash = 깜빡임

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()
