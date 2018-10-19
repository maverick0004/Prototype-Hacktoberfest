from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os.path

def send():
    
    EMAIL = email.get()
    PASSWORD = password.get()
    EMAIL_TO = to.get()
    recepients = EMAIL_TO.split(',')

    msg = MIMEMultipart()
    msg['From'] = EMAIL
    msg['To'] = EMAIL_TO
    msg['Subject'] = subject.get()
    
    body = message.get("1.0",END)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()       # Extended Hello
    server.starttls()   # Put the SMTP connection in TLS (Transport Layer Security) mode.  
    server.ehlo()       # All SMTP commands that follow will be encrypted.

    server.login(EMAIL, PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL, recepients, text)
    server.quit()

master = Tk()
master.title("GMail")

project_root = os.path.abspath(os.path.join("./", os.pardir))
logo = PhotoImage(file=project_root+"/images/Webp.net-resizeimage.png")
Label(master, image=logo, bd=0,anchor=CENTER).grid(row=0,sticky=N,pady=20,column=1)

Label(master, text="Email Id:",font=("Helvetica",14)).grid(row=1, column=0,sticky=E,pady=10)
email = StringVar()
Entry(master, textvariable=email,font=("Helvetica",14),width=80).grid(row=1, column=1,pady=10,padx=10)

Label(master, text="Password:",font=("Helvetica",14)).grid(row=2, column=0,sticky=E,pady=10)
password = StringVar()
Entry(master, textvariable=password, show='*',font=("Helvetica",14),width=80).grid(row=2, column=1,pady=10,padx=10)

Label(master, text="To:",font=("Helvetica",14)).grid(row=3, column=0,sticky=E,pady=10)
to = StringVar()
Entry(master, textvariable=to,font=("Helvetica",14),width=80).grid(row=3, column=1,pady=10,padx=10)

Label(master, text="Subject:",font=("Helvetica",14)).grid(row=4, column=0,sticky=E,pady=10)
subject = StringVar()
Entry(master, textvariable=subject,font=("Helvetica",14),width=80).grid(row=4, column=1,pady=10,padx=10)

Label(master, text="Message:",font=("Helvetica",14)).grid(row=5, column=0,sticky=E,pady=10)
message = Text(master,font=("Helvetica",14))
message.grid(row=5, column=1,pady=10,padx=10)

send = Button(master, text="SEND",command=send, bd=0,pady=20,font=("Helvetica",14),width=80).grid(row=6,column=1,sticky=N,padx=10)

master.mainloop()