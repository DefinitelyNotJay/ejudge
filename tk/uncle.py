""" GUI-wall-v1.py """

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title("โปรแกรมคำนวน v.1")
GUI.geometry("800x600")

FONT1 = ("TH SarabunPSK", 24)
FONT2 = ("TH SarabunPSK", 30, 'bold')

F1 = Frame(GUI)
F1.place(x=50, y=50)

# WIDTH

# image = PhotoImage(file='C:\Users\ASUS\Desktop\e-judge\python\tk').subsample(6)

# L0 = Label(F1, image=image)
# L0.pack()

L1 = Label(F1, text="ความกว้างผนัง", font=FONT1)
L1.pack()

v_width = StringVar()
E1 = ttk.Entry(F1, font=FONT1, textvariable = v_width)
E1.pack()

# HEIGHT
L2 = Label(F1, text="ความสูงผนัง", font=FONT1)
L2.pack()

v_height = StringVar()
E2 = ttk.Entry(F1, font=FONT1, textvariable = v_height)
E2.pack()

# BUTTON
B1 = ttk.Button(F1, text="คำนวณ")
B1.pack(ipadx=30, ipady=20, pady=20)

v_result = StringVar()
v_result.set('ผนังกว้าง 5x5 m')
R1 = Label(F1, textvariable=v_result, font=FONT1)
R1.pack()

# Frame2
F2 = Frame(GUI)
F2.place(x=500, y=50)

L3 = Label(F2, text='รวมค่าใช้จ่ายทั้งหมด', font=FONT1, fg="green")
L3.pack()

text = "ผนังกว้าง 5x5 m"

v_result2 = StringVar()
v_result2.set('ผนังกว้าง 5x5 m')
R2 = Label(F2, textvariable=v_result2, font=FONT1)
R2.pack()

v_result3 = StringVar()
v_result3.set('รวมทั้งหมด : 6000 บาท')
R3 = Label(F2, textvariable=v_result3, font=FONT2)
R3.pack()

#Frame 3
F3 = Frame(GUI)
F3.place(x=500, y=450)
L3 = Label(F3, text="ราคาต่อหน่วย (บาท/ตร.ม.)", font=FONT1)
L3.grid(row=0, column=0)

v_price = StringVar()
v_price.set('100')
E3 = ttk.Entry(F3, font=FONT1, textvariable = v_price, width=5)
E3.grid(row=0, column=1)

FB = Frame(GUI)
FB.place(x=600, y=500)
B2 = ttk.Button(FB, text="reset")
B2.pack(ipadx=30, ipady=20, pady=20)
GUI.mainloop()
