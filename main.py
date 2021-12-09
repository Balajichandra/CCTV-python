from tkinter import *
from PIL import Image,ImageTk
from record import record
windows = Tk()
windows.title("Live CCTV Recording")
windows.iconphoto(True,PhotoImage(file="main.png"))
windows.geometry('1080x720')
#main frame
mainFrame = Frame(windows,bd=2)
label_title = Label(mainFrame,text="Live 24X7 Survillance Area",font=('Helvitica',40,'bold'))
label_title.grid(pady=(10,10),column=1)

icon_1 = Image.open("24.png")
icon_1 = icon_1.resize((70,70),Image.ANTIALIAS)
icon_1 = ImageTk.PhotoImage(icon_1)
label_icon1 = Label(mainFrame,image=icon_1)
label_icon1.grid(row=0,pady=(5,10),column=0)

icon_spy = Image.open("spa.png")
icon_spy = icon_spy.resize((180,180),Image.ANTIALIAS)
icon_spy = ImageTk.PhotoImage(icon_spy)
label_icon_spy = Label(mainFrame,image=icon_spy)
label_icon_spy.grid(row=1,pady=(5,10),column=1)

btn_img = Image.open("recording.png")
btn_img = btn_img.resize((50,50),Image.ANTIALIAS)
btn_img = ImageTk.PhotoImage(btn_img)
btn = Button(mainFrame,text="VideoRecord",font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=btn_img,compound="left",command=record)
btn.grid(row=2,pady=(20,10),column=1)

btn_exit = Image.open("exit.png")
btn_exit = btn_exit.resize((50,50),Image.ANTIALIAS)
btn_exit = ImageTk.PhotoImage(btn_exit)
btn_xt = Button(mainFrame,text="Exit",font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=btn_exit,compound="left",command=windows.quit)
btn_xt.grid(row=3,pady=(20,10),column=1)
mainFrame.pack()
windows.mainloop()