from tkinter import *
import cv2
import pyzbar.pyzbar as pyzbar
from tkinter import filedialog
from PIL import ImageTk

root = Tk()
root.title("QR-Code Scanner")
root.geometry("900x500+200+80")
root.config(bg="white")


def browseFiles():
    global img
    global img1
    f_types = [('Png Files', '*.png')]
    file_name = filedialog.askopenfilename(initialdir = "C:/Users/abc/Desktop/Qr code/QR Codes", title="Select a File",
                                           filetypes=f_types)
    if file_name != "":
        img = ImageTk.PhotoImage(file=file_name)
        l1 = Label(f1, image=img)
        l1.place(x=100, y=50)
        img1 = cv2.imread(file_name)
        button2.config(state=NORMAL)


def Sub():
    decode_obj = pyzbar.decode(img1)
    for x in decode_obj:
        d = x.data
        Label(f1, text=d,font=("times new roman",15)).place(x=100, y=320)


f1 = Frame(root, bd=2, width=450, height=400, relief=GROOVE)
f1.place(x=220,y=80)

l3 = Label(root,text="Scan Your QR-Code", bg="#9c08c9", fg="white",font=("times roman new", 15, "bold"))
l3.place(x=0,y=0,relwidth=1,height=35)

button2 = Button(f1,text="Check Detail",state=DISABLED,relief=RAISED, bg="#b7b2b8", bd=2, cursor="hand2",
                 font=("times roman new", 12, "bold"), activebackground="#b7b2b8", command=Sub)
button2.place(x=170, y=10)

button1 = Button(root, text="Browse Files",relief=RAISED, bg="#040405",fg="white",  bd=2, cursor="hand2",
                 font=("times roman new", 12, "bold"), activebackground="#040405",activeforeground="white", command=browseFiles)
button1.place(x=370, y=40, width=150)

root.mainloop()

# ---------------------------------------------------------------------------------------





# cv2.imshow("Image",img)
# cv2.waitKey(0)
