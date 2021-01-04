import smtplib
from tkinter import *
from string import Template
from tkinter import messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def main():
    try:
        print("this is command line interface to send emails")
        print("--------------------------------------------------------------------------------------------------------------")
        MY_ADDRESS = username.get()
        print(MY_ADDRESS)
        PASSWORD = password__login_entry.get()
        print(PASSWORD)
        name3_str = name__login_entry.get()
        name4_str = email__login_entry.get()
        massag=massage__login_entry.get("1.0", "end-1c") 
        names = []
        names.append(name3_str)
        emails = []
        emails.append(name4_str)
    

        # set up the SMTP server
        s = smtplib.SMTP(host='smtp.gmail.com', port=587)
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
        for name, email in zip(names, emails):
            msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
       
            message=massag
        # Prints out the message body for our sake
            print(message)

        # setup the parameters of the message
            msg['From']=MY_ADDRESS
            msg['To']=email
            msg['Subject']=s__login_entry.get()
        
        # add in the message body
            msg.attach(MIMEText(message, 'plain'))
        
        # send the message via the server set up earlier.
            s.send_message(msg)
            del msg
        
    # Terminate the SMTP session and close the connection
        s.quit()
    except:
        

# message box display
        messagebox.showerror("Error", "please try again somthig went wrong")
        
        messagebox.showinfo("Information","write your email name and password correctly and check the connection")
       

        
if __name__ == '__main__':

    
    login_screen=Tk()
    login_screen.title("SEND EMAIL")
    login_screen.geometry("400x450")
    Label(login_screen, text="CMD LINE INTERFACE FOR SEMDING MAIL").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="EMAIL:").pack()
    username = Entry(login_screen, textvariable="EMAIL",width=32)
    username.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password:").pack()
    password__login_entry = Entry(login_screen, textvariable="password", show= '*',width=32)
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Mail of reciver:").pack()
    email__login_entry = Entry(login_screen, textvariable="text",width=32)
    email__login_entry.pack()
    Label(login_screen, text="name of reciver:").pack()
    name__login_entry = Entry(login_screen, textvariable="reciver",width=32)
    name__login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="subject").pack() 
    s__login_entry = Entry(login_screen, textvariable="subjecttext",width=32)
    s__login_entry.pack()
    Label(login_screen, text="massage:").pack()
    massage__login_entry = Text(login_screen, height = 5, width = 32) 
    massage__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="SEND", width=10, height=1,command = main).pack()
    login_screen.mainloop()
    