from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("การคำนวณพื้นที่สี่เหลี่ยมผืนผ้า")

myLable1 = Label(root,text="ใส่ความกว้าง").grid(row=0)
ความกว้าง = IntVar()
et1 = Entry(textvariable=ความกว้าง)
et1.grid(row=1,column=1)

myLable2 = Label(root,text="ใส่ความสูง").grid(row=2)
ความสูง = IntVar()
et2 = Entry(textvariable=ความสูง)
et2.grid(row=3,column=1)

Label(text="ค่าของพื้นที่").grid(row=4)
et3 = Entry(text="พื้นที่")
et3.grid(row=5,column=1)

def area():
    w = ความกว้าง.get()
    h = ความสูง.get()
    area = w*h
    et3.insert(0,area)

bt = Button(root,text="คำนวณ",command=area).grid(row=6,column=1,sticky=W)

root.geometry("200x200")
root.mainloop()