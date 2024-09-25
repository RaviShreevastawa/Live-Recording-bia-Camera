from tkinter import*
from PIL import Image,ImageTk
from record import record

window = Tk()
window.title("Live CCtv Camera")
window.iconphoto(False,PhotoImage(file='recordings.png'))
window.geometry('1080x600')

# Main Frame
mainFrame = Frame(window,bd=2)

label_title = Label(mainFrame,text="Live CCtv Camera",font=('Helvitika',40,'bold'))
label_title.grid(pady=(10,10),column=1)

icon_1 = Image.open("Icons/24.png")
icon_1 = icon_1.resize((70,70),Image.Resampling.LANCZOS)
icon_1 = ImageTk.PhotoImage(icon_1)
label_icon_1 = Label(mainFrame,image=icon_1)
label_icon_1.grid(row=0,pady=(5,10),column=0)

icon_spy = Image.open("Icons/spa.png")
icon_spy = icon_spy.resize((180,180),Image.Resampling.LANCZOS)
icon_spy = ImageTk.PhotoImage(icon_spy)
label_icon_spy = Label(mainFrame,image=icon_spy)
label_icon_spy.grid(row=1,pady=(5,10),column=1)

# Recording Button
btn_image = Image.open("Icons/recording.png")
btn_image = btn_image.resize((50,50),Image.Resampling.LANCZOS)
btn_image = ImageTk.PhotoImage(btn_image)

btn = Button(mainFrame,text='VideoRecord',font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=btn_image,compound='left',command=record)
btn.grid(row=2,pady=(20,10),column=1)

# Exit Button
btn_image1 = Image.open("Icons/exit.png")
btn_image1 = btn_image1.resize((50,50),Image.Resampling.LANCZOS)
btn_image1 = ImageTk.PhotoImage(btn_image1)

btn_exit = Button(mainFrame,text='Exit',font=('Helvitica',25,'bold'),height=90,width=270,fg='orange',image=btn_image1,compound='left',command=window.quit)
btn_exit.grid(row=3,pady=(20,10),column=1)

mainFrame.pack()

window.mainloop()