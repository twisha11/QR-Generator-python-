from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage
import os
from tkinter import messagebox

class Register:
    def __init__(self,root):
        self.root = root  # intializaion root
        self.root.title("QR-Code Generator")
        self.root.geometry("930x600+30+10")
        self.root.config(bg="white")

        self.f1 = Frame(self.root,bg="#f0f0f0", bd=2, relief=GROOVE, )
        self.f1.place(x=30,y=50,width=500, height=500)

        main_l1 = Label(self.f1,text="Enter Your Information", font=("times roman new",15,"bold"),
                        bg="#9c08c9", fg="#ffffff")
        main_l1.place(x=0,y=0,width=496,height=40)

        l1 = Label(self.f1, text="Enter your Name", font=("times roman new", 15, "bold"))
        l1.place(x=10, y=100)

        self.var_e1=StringVar()
        self.e1 = Entry(self.f1, textvariable=self.var_e1, font=("times roman new", 12))
        self.e1.place(x=200,y=100,width=200, height=30)

        l1 = Label(self.f1, text="Enter your ID", font=("times roman new", 15, "bold"))
        l1.place(x=10, y=150)

        self.var_e2 = StringVar()
        self.e2 = Entry(self.f1,textvariable=self.var_e2, font=("times roman new", 12))
        self.e2.place(x=200, y=150, width=200, height=30)

        l3 = Label(self.f1, text="Enter Department", font=("times roman new", 15, "bold"))
        l3.place(x=10, y=200)

        self.var_e3 = StringVar()
        self.e3 = Entry(self.f1,textvariable=self.var_e3, font=("times roman new", 12))
        self.e3.place(x=200, y=200, width=200, height=30)

        btn_submit=Button(self.f1,text="Genrate QR Image",relief=RAISED, bg="#9c08c9", bd=2,cursor="hand2",
                          fg="#ffffff",font=("times roman new", 15,"bold"),activebackground="#9c08c9",
                          activeforeground="white", command=self.generate)
        btn_submit.place(x=100,y=300)

        btn_clr = Button(self.f1, text="Clear", relief=RAISED, bg="#b7b2b8", bd=2, cursor="hand2",
                             font=("times roman new", 15, "bold"), activebackground="#b7b2b8", command=self.clear)
        btn_clr.place(x=300, y=300,width=150)

        self.l4 = Label(self.f1)
        self.l4.place(x=40, y=400)

        self.f2 = Frame(self.root, bd=2, width=350, height=500, relief=GROOVE)
        self.f2.place(x=550, y=50)

        main_l2 = Label(self.f2, text="Your Information", font=("times roman new", 15, "bold"),
                        bg="#9c08c9", fg="#ffffff")
        main_l2.place(x=0, y=0, width=345, height=40)

        self.qr_lbl = Label(self.f2,text="QR-Code\n Not Available",bg="#bf57d4",
                       font=("times roman new", 15, "bold"),relief=SUNKEN)
        self.qr_lbl.place(x=50,y=120,width=250,height=250)

        btn_scan = Button(self.root, text="To Scan your Qr-code..", cursor="hand2",bd=0,bg="white",
                          font=("times roman new", 15, "bold"),command=self.scan)
        btn_scan.place(x=680, y=555)

    def clear(self):
        self.var_e1.set('')
        self.var_e2.set('')
        self.var_e3.set('')
        self.l4.config(text=" ")
        self.qr_lbl.config(image="")

    def generate(self):
        if self.e1.get()=='' or self.e2.get()=='' or self.e3.get()=='':
            self.l4.config(text='ALL FIELD ARE REQUIRED TO FILL', font=("times roman new", 15), fg="red")

        else:
            qr_data=(f"Employee Name:{self.var_e1.get()}\n,Employee ID :{self.var_e2.get()}\n,"
                     f"Employee Department:{self.var_e3.get()}")
            f_name= ("Emp_"+str(self.var_e2.get())+'.png')
            folder = os.path.isfile(f"C:/Users/abc/Desktop/Qr code/QR Codes/{f_name}")
            if folder == TRUE:
                messagebox.showerror("Error", "You Already Generated QR-CODE")
            else:
                qr_code = qrcode.make(qr_data)
                qr_code = resizeimage.resize_cover(qr_code, [249, 249])
                qr_code.save("QR Codes/Emp_" + str(self.var_e2.get() + '.png'))
                self.img = ImageTk.PhotoImage(file="QR Codes/Emp_" + str(self.var_e2.get() + '.png'))
                self.qr_lbl.config(image=self.img)
                self.l4.config(text="QR-CODE SUCCESSFULLY GENERATED", font=("times roman new", 15), fg="green")

    def scan(self):
        root.destroy()
        import scan







root = Tk()

obj = Register(root)  # 'Register' class nu obj che

root.mainloop()


