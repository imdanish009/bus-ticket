from tkinter import *
from tkinter import Tk, StringVar ttk
from tkinter import random
from tkinter import messagebox
import time;
import datetime
from tkinter import font


root = Tk()
root.geometry("1350x750+0+0")
root.title("Bus Ticket")
root.configure(background='#FFA07A')



Top= Frame(root, width=1350, height=100, bd=20, relief='raise')
Top.pack(side=TOP)

f2=Frame(root, width=1000, height=650, bd=2, relief="raise",pady=10)
f2.pack(side=TOP)


f3=Frame(root, width=150, height=40, bd=2, relief="raise",pady=10)
f3.pack(side=TOP)

#---------------------------------------------frame,title -------------------------------------------

Top.configure(background='#FFA07A')
f2.configure(background='#FFA07A')
f2.configure(background='pink')
lb1Title=Label(Top,font=('italic',40,'bold'),text="Bus Ticketing system ",bd=5,fg="#FF4081", width=41, justify='center')
lb1Title.grid(row=0,column=0)


#==============================================receipt===========


lblReceipt = Label(f2,font=('italic',20,'bold'),text="RECEIPT DETAIL:",fg='blue', justify='center', bd=8).grid(row=0,column=0 ,sticky=W)
txtReceipt = Text(f2,font=('italic' ,16, 'bold') , bd=8 ,width=50,height=15 ,state=DISABLED)
txtReceipt.grid(row=1,column=0)

#====================================BOTTON PRINT=============

btnPrint= Button (f3, text='PRINT',padx=2,pady=2,bd=2, fg='#00B8D4', font=('italic', 12, 'bold'), width=8,
                  height=1).grid(row=1, column=0)
#===============================================================================================


"""              
def Receipt():
    txtReceipt.delete("1.0",END)
    txtReceipt.insert(END,'Receipt Ref:\t\t\t'+Receipt_Ref.get()+'\t\t'+datet.get()+'\t\t'+time1.get()+'\n')
    txtReceipt.insert(END,'CLASS:\t\t\t'+"Class:\n\n")
    txtReceipt.insert(END,'Ticket:\t\t\t\t'+Ticketclass.get()+'\t\t'+'\n')
"""    








root.mainloop()
