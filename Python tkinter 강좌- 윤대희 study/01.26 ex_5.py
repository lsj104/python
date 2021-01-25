import tkinter

window=tkinter.Tk()
window.title("EX_5")
window.geometry("640x400+100+100")
window.resizable(False,False)

listbox = tkinter.Listbox(window, selectmod='extended,', height = 0)
listbox.insert(0,"no.1")
listbox.insert(1,"no.2")
listbox.insert(2,"no.2")
listbox.insert(3,"no.2")
listbox.insert(4,"no.3")
listbox.delete(1,2) #단일 항목만 삭제
listbox.pack()

window.mainloop()

