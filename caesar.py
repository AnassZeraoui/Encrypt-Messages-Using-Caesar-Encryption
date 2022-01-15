#caesar cypher encryption project using Tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import pyperclip

#configuring infos about the caesar encryption
def click():
    messagebox.showinfo("Infos","The Caesar Cipher technique is one of the earliest and simplest method of encryption technique. It’s simply a type of substitution cipher, i.e., each letter of a given text is replaced by a letter some fixed number of positions down the alphabet")
#configuring the caesar encoding or decoding :
def caesar():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    a = type.get()
    s = int(current_value.get())
    text=message_entry.get()
    if a=="encode":
        c['text']=""
        cipher_text=""
        for index in text:
            if index in alphabet:
                position = alphabet.index(index)
                new_posi = position + s
                cipher_text += alphabet[new_posi]
            else:
                cipher_text += index
        c['text']+=f"{cipher_text}"
        pyperclip.copy(cipher_text)
    else:
        c['text']=""
        cipher_text = ""
        for index in text:
            if index in alphabet:
                position = alphabet.index(index)
                new_position = position - s
                cipher_text += alphabet[new_position]
            else:
                cipher_text += index
        c['text'] +=f"{cipher_text}"
        pyperclip.copy(cipher_text)

#tkinter basic configuration :
window = Tk()
window.title("Caesar Encryption")
window.config(bg="white")
window.minsize(650,550)
window.maxsize(650,550)
window.iconbitmap('C:\\Users\\Ziraoui_Anas\\Desktop\\resume\\caesar encryption tkinter\\newico.ico')
list=["encode","Decode"]
#configuring labels:
Label(window,text="Welcome to the oldest Encryption technique",font=("courier",12,"bold"),bg="white").place(x=130,y=20)
Label(window,text="for more infos.",font=("courier",12,"bold"),bg="white").place(x=170,y=60)
Label(window,text="Encrypt or Decrypt:",font=("courier",12,"bold"),bg="white").place(x=60,y=135)
Label(window,text="Type the message:",font=("courier",12,"bold"),bg="white").place(x=60,y=195)
Label(window,text="Shift number : ",font=("courier",12,"bold"),bg="white").place(x=60,y=255)
Label(window,text=f"Cipher Text:",font=("courier",12,"bold"),bg="white").place(x=60,y=315)
c = Label(window,text="",font=("courier", 12, "bold"), bg="white")
c.place(x=260, y=315)
#configuring the canvas : 
image = Image.open("logo.png")
image = image.resize((90,90))
caesar_canvas = Canvas(window,width=90,height=90)
caesar_canvas.image=ImageTk.PhotoImage(image)
caesar_canvas.create_image(0,0,image=caesar_canvas.image,anchor=NW)
caesar_canvas.place(x=19,y=15)
#configuring combobox
type = ttk.Combobox(window,values=list)
type.place(x=260,y=135,width=200)
type.bind('<<ComboboxSelected>>')
#configuring Entries:
message_entry=Entry(window,text="",font=("courier",12,"bold"),bg="white")
message_entry.place(x=260,y=195,width=350)
#configuring Spinbox:
current_value=StringVar(value="Choose a category")
shift =ttk.Spinbox(window,textvariable=current_value,from_=1,to=100,font=("courier",12)).place(x=260,y=255)
#configuring buttons,
Button(window,text="Click here!",font=("courier",12,'bold'),bg="white",relief=FLAT,command=click).place(x=330,y=56)
Button(window,text="Enrypt or Decrypt",font=("courier",12,"bold"),bg="silver",relief=FLAT,command=caesar).place(x=100,y=375)
Button(window,text="Quit",font=("courier",12,"bold"),bg="silver",relief=FLAT,command=window.destroy).place(x=340,y=375,width=160)
window.mainloop()
