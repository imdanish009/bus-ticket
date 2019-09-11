from tkinter import *


root = Tk()
root.geometry("1350x750+0+0")
root.title("Bus Ticket details")
root.configure(background='orange')


Top= Frame(root, width=1350, height=100, bd=20, relief='raise')
Top.pack(side=TOP)

f2=Frame(root, width=1000, height=750, bd=2, relief="raise",pady=10)
f2.pack(side=TOP)

txtSubmit = Text(f2,font=('italic' ,16, 'bold') ,bd=8,bg="light green",width=110,height=100)
txtSubmit.grid(row=1,column=0)



#---------------------------------------------frame,title -------------------------------------------

Top.configure(background='orange')
f2.configure(background='#FFA07A')


lb1Title=Label(Top,font=('italic',18,'bold'),text="Bus Ticket Details ",bd=5,fg="#FF4081", width=100,height=1, justify='center')
lb1Title.grid(row=0,column=0)

#==============================================receipt===========
a=open("slip.doc","r")
y=a.read()
txtSubmit.insert(END,y)
a.close()



def iExit():
    qExit= tkMessageBox.askyesno("QUIT SYSTEM","DO YOU WANT TO QUIT ?")
    if qExit ==True:
        root.destroy()
        return


    


root.mainloop()
