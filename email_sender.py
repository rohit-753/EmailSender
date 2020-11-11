import smtplib
from tkinter import *
bg='#f1c159'
fg='#2b2b2b'

sender='sendermail@gmail.com'
password='Sender_Password'
def send_mail(reciver,message):
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender,password)
    s.sendmail(sender,reciver,message)
    s.quit()
root=Tk()
root.geometry("500x400")
root.configure(bg = bg)
root.title('Rohit Mail Service')

Label(root,text="Email Sender",font=("Helvetica",20),fg=fg,bg=bg).place(x=120,y=10)
Label(root,text="Send To",font=("Helvetica",10),fg=fg,bg=bg).place(x=30,y=70)
Label(root,text="Message:",font=("Helvetica",10),fg=fg,bg=bg).place(x=25,y=110)

#Label(root,text="Email Sender").place(x=120,y=10)
#Label(root,text="Send To").place(x=30,y=70)
#Label(root,text="Message:").place(x=25,y=110)

rec_name=Entry(root,width=30)
rec_name.place(x=120,y=70)
msg=Text(root,height=10,width=30)
msg.place(x=120,y=110)
Button(root,text="  Send  ",command=lambda: send_mail(rec_name.get(),msg.get("1.0",END))).place(x=120,y=330)
root.mainloop()