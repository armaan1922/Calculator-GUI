from tkinter import *
from tkinter import messagebox
val = ""
operator=""
A = 0

def btn1_clicked():
    global val
    val = val +"1"
    data.set(val)

def btn2_clicked():
    global val
    val = val +"2"
    data.set(val)

def btn3_clicked():
    global val
    val = val +"3"
    data.set(val)

def btn4_clicked():
    global val
    val = val +"4"
    data.set(val)

def btn5_clicked():
    global val
    val = val +"5"
    data.set(val)

def btn6_clicked():
    global val
    val = val +"6"
    data.set(val)

def btn7_clicked():
    global val
    val = val +"7"
    data.set(val)

def btn8_clicked():
    global val
    val = val +"8"
    data.set(val)

def btn9_clicked():
    global val
    val = val +"9"
    data.set(val)

def btnzero():
    global val
    val = val + "0"
    data.set(val)


def btndmul_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator="*"
    val = val +"*"
    data.set(val)


def btnplus_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btnmin_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btndiv_clicked():
    global val
    global operator
    global A
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def cancel():
    global val
    global operator
    val = ""
    operator=""
    data.set(val)


def result():
    global val
    global operator
    global A
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A+x
        data.set(c)
        val = str(c)
    if operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("error,sir g 0 nal divide ni kreeda")
            A = ""
            val = ""
            data.set(c)
        else:
              c = A / x
              data.set(c)
              val = str(c)







screen = Tk()

screen.title("Armaan's calculator")
screen.geometry("400x550")
screen.resizable(0,0)

data = StringVar()



#label1 = Label(text="You can calculate anything in this calculator!",padx="500",
             # font="comicsansms 13 italic", bg="white", fg="blue")
#label1.pack()

label2 = Label(screen,anchor = "se",relief="groove",border="5",font="verdana,70,bold",fg="blue",
               textvariable=data,

               pady="20",padx="10")
label2.pack(expand = True,fill = "both")

btnrow1 = Frame(screen)
btnrow1.pack(expand=True,fill="both")

btnrow2 = Frame(screen)
btnrow2.pack(expand=True,fill="both")

btnrow3 = Frame(screen)
btnrow3.pack(expand=True,fill="both")

btnrow4 = Frame(screen)
btnrow4.pack(expand=True,fill="both")





btn7 = Button(btnrow1,text = "7",font ="verdana 24 italic",relief="groove",border="0",
              command=btn7_clicked)
btn7.pack(side=LEFT,expand=True,fill="both")

btn8 = Button(btnrow1,text = "8",font ="verdana 24 italic",relief="groove",border="0",
              command=btn8_clicked)
btn8.pack(side=LEFT,expand=True,fill="both")

btn9 = Button(btnrow1,text = "9 ",font ="verdana 24 italic",relief="groove",border="0",
              command=btn9_clicked)
btn9.pack(side=LEFT,expand=True,fill="both")

btnprcnt = Button(btnrow1,text = "%",font ="verdana 18 italic",relief="groove",border="0"
              ,fg="blue",bg="grey")

btnprcnt.pack(side=LEFT,expand=True,fill="both")

btncncl=Button(btnrow1,text = "c",font ="verdana 20 italic",relief="groove",border="0"
            ,fg="red",bg="grey",command=cancel)
btncncl.pack(side=LEFT,expand=True,fill="both")


btn6 = Button(btnrow2,text = "6",font ="verdana 24 italic",relief="groove",border="0",
              command=btn6_clicked)
btn6.pack(side=LEFT,expand=True,fill="both")

btn5 = Button(btnrow2,text = "5",font ="verdana 24 italic",relief="groove",border="0",
              command=btn5_clicked)
btn5.pack(side=LEFT,expand=True,fill="both")

btn4 = Button(btnrow2,text = "4",font ="verdana 24 italic",relief="groove",border="0",
              command=btn4_clicked)
btn4.pack(side=LEFT,expand=True,fill="both")

btndiv= Button(btnrow2,text = "/",font ="verdana 20 italic",relief="groove",border="0",
              fg="blue",bg="grey",command=btndiv_clicked)
btndiv.pack(side=LEFT,expand=True,fill="both")

btnmul=Button(btnrow2,text = "*",font ="verdana 20 italic",relief="groove",border="0",
              command=btndmul_clicked
            ,fg="blue",bg="grey")
btnmul.pack(side=LEFT,expand=True,fill="both")


btn1 = Button(btnrow3,text = "1",font ="verdana 24 italic",relief="groove",border="0",
              command=btn1_clicked)
btn1.pack(side=LEFT,expand=True,fill="both")

btn2 = Button(btnrow3,text = "2",font ="verdana 24 italic",relief="groove",border="0",
              command=btn2_clicked)
btn2.pack(side=LEFT,expand=True,fill="both")

btn3 = Button(btnrow3,text = "3 ",font ="verdana 24 italic",relief="groove",border="0",
              command=btn3_clicked)
btn3.pack(side=LEFT,expand=True,fill="both")

btnplus = Button(btnrow3,text = "+",font ="verdana 18 italic",relief="groove",border="0",
                 command=btnplus_clicked
              ,fg="blue",bg="grey")
btnplus.pack(side=LEFT,expand=True,fill="both")

btnmin=Button(btnrow3,text = "-",font ="verdana 24 italic",relief="groove",border="0",
              command=btnmin_clicked
            ,fg="blue",bg="grey")
btnmin.pack(side=LEFT,expand=True,fill="both")



btnsqrt = Button(btnrow4,text = "sqrt",font ="verdana 20 italic",relief="groove",border="0",)
btnsqrt.pack(side=LEFT,expand=True,fill="both")

btn0 = Button(btnrow4,text = "0",font ="verdana 24 italic",relief="groove",border="0",
              command=btnzero)
btn0.pack(side=LEFT,expand=True,fill="both")

btndot = Button(btnrow4,text = ".",font ="verdana 30 italic",relief="groove",border="0",)
btndot.pack(side=LEFT,expand=True,fill="both")


btneql =Button(btnrow4,text = " = ",font ="verdana 38 italic",relief="groove",border="0",
             fg="white",bg="black",command=result)
btneql.pack(side=LEFT,expand=True,fill="both")









label0 = Label(screen,text = "Designed by--> ARMAANDEEP SINGH\n contact number->9876349323",
           anchor = "se", font ="arial 10 italic",pady="20",padx="10")
label0.pack(anchor="se")

screen.mainloop()