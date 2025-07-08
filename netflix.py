from tkinter import *
from PIL import ImageTk ,Image
from tkinter import messagebox

root= Tk()
def toggle():
    if password_input.cget('show') == '':
        password_input.config(show='*')
        show_button.config(text='Show')
    else:
        password_input.config(show='')
        show_button.config(text='Hide')

def login():
    username = username_input.get()
    password = password_input.get()

    if username == "abc" and password == "123":
        messagebox.showinfo("Login Successful", "Welcome to Netflix!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")


root.title("NETFLIX LOGIN")
root.iconbitmap("favicon.ico")
root.geometry("350x250")
root.minsize(150,150)
root.maxsize(500,500)
root.configure(bg="#141414")

#img=ImageTk.PhotoImage(Image.open("background.jpg"))
#img_label= Label(root,image=img)
#img_label.pack()
text_label = Label(root, text="NETFLIX", fg="red", bg="#141414", font=("Arial Black", 24))
text_label.pack(pady=10)


username_label=Label(root,text="Username", fg="white", bg="#141414", font=("Arial", 10))
username_label.pack(pady=5)
username_input=Entry(root, width=30)
username_input.pack()


password_label=Label(root,text="Password", fg="white", bg="#141414", font=("Arial", 10))
password_label.pack(pady=5)
password_frame=Frame(root,bg="#141414")
password_frame.pack()
password_input=Entry(password_frame, width=30 ,show='*')
password_input.grid(row=0,column=0)


show_button = Button(password_frame, text="Show", command=toggle, bg="gray", fg="white", height=1)
show_button.grid(row=0,column=1,padx=5)

login_btn = Button(root, text="Login",command=login, bg="red", fg="white", width=20)
login_btn.pack(pady=15)


                       

root.mainloop()
#root.title("NETFLIX LOGIN")
