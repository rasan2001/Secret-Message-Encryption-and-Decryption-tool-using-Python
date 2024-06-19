from tkinter import *
from tkinter import messagebox
import base64

def decrypt():
    password=code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#007bff")

        message=text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")

        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#007bff").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10" , bg="white", relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")

    elif password != "1234":
        messagebox.showerror("encryption","Invalid Password")

def encrypt():
    password=code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#28a745")

        message=text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")

        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#28a745").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10" , bg="white", relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","please enter the password")

    else:
        messagebox.showerror("encryption","Invalid Password")        



def main_screen():

    global screen
    global code
    global text1

    def reset():
        code.set("")
        text1.delete(1.0,END)

    # Create the main application window
    screen = Tk()
    screen.geometry("375x500")
    screen.configure(bg="#f8f9fa")

    # Set the window title
    screen.title("Text Encryptor/Decryptor")

    # Header
    header = Frame(screen, bg="#343a40")
    header.pack(fill=X)
    Label(header, text="Text Encryptor and Decryptor", fg="white", bg="#343a40", font=("Helvetica", 18, "bold")).pack(pady=10)

    # Main Container
    main_container = Frame(screen, bg="#f8f9fa", padx=20, pady=20)
    main_container.pack(expand=True, fill=BOTH)

    # Text Input
    Label(main_container, text="Enter text:", fg="#495057", bg="#f8f9fa", font=("Arial", 12, "bold")).pack(anchor=W)
    text1 = Text(main_container, font=("Arial", 12), bg="white", relief=RIDGE, wrap=WORD, bd=2, height=6)
    text1.pack(expand=True, fill=BOTH, pady=10)

    # Password Input
    Label(main_container, text="Enter password:", fg="#495057", bg="#f8f9fa", font=("Arial", 12, "bold")).pack(anchor=W)
    code = StringVar()
    Entry(main_container, textvariable=code, width=25, bd=2, font=('Arial', 14), show="*").pack(pady=5)

    # Button Container
    button_container = Frame(main_container, bg="#f8f9fa")
    button_container.pack(pady=20)

    # Buttons
    encrypt_btn = Button(button_container, text="ENCRYPT", height=2, width=12, bg="#28a745", fg="white", bd=0, font=("Arial", 10, "bold"), command=encrypt)
    encrypt_btn.grid(row=0, column=0, padx=10)
    decrypt_btn = Button(button_container, text="DECRYPT", height=2, width=12, bg="#007bff", fg="white", bd=0, font=("Arial", 10, "bold"), command=decrypt)
    decrypt_btn.grid(row=0, column=1, padx=10)
    reset_btn = Button(button_container, text="RESET", height=2, width=26, bg="#6c757d", fg="white", bd=0, font=("Arial", 10, "bold"), command=reset)
    reset_btn.grid(row=1, columnspan=2, pady=10)


    # Run the main loop
    screen.mainloop()

if __name__ == "__main__":
    main_screen()
