from fileinput import filename
from multiprocessing.resource_sharer import stop
from tkinter import *
import pyscreenrec

root=Tk()
root.title("Screen Recoder")
root.geometry("370x600")
root.resizable(False,False)
root.configure(bg="white")

def start_rec():
    file=Filename.get()
    rec.start_recording(str(file+".mp4"),5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()


def stop_rec():
    rec.stop_recording()


rec=pyscreenrec.ScreenRecorder()

#icon
root.iconbitmap("favicon.ico")

#heading
lbl=Label(root,text="Screen Recoder",bg="white",font="arial 15 bold")
lbl.pack(pady=20)



image1=PhotoImage(file="C:/Users/ahnaf/Documents/Pycharm Projects/screen_recoder/recod.png")
Label(root,image=image1,bd=0).pack(pady=30)

#Entry
Filename=StringVar()
entry=Entry(root,textvariable=Filename,width=18,font="arial 15")
entry.place(x=100,y=350)
Filename.set("type record name")

#buttons
start=Button(root,text="Start",font="arial 15",bd=0,command=start_rec)
start.place(x=150,y=300)

image2=PhotoImage(file="C:/Users/ahnaf/Documents/Pycharm Projects/screen_recoder/pause.png")
pause=Button(root,image=image2,bd=0,bg="white",command=pause_rec)
pause.place(x=50,y=450)

image3=PhotoImage(file="C:/Users/ahnaf/Documents/Pycharm Projects/screen_recoder/resume.png")
resume=Button(root,image=image3,bd=0,bg="white",command=resume_rec)
resume.place(x=150,y=450)

image4=PhotoImage(file="C:/Users/ahnaf/Documents/Pycharm Projects/screen_recoder/stop.png")
stop=Button(root,image=image4,bd=0,bg="white",command=stop_rec)
stop.place(x=250,y=450)

root.mainloop()