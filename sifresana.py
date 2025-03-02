import tkinter as tk
import random

root = tk.Tk()
root.title("Šifrēšana")

label = tk.Label(root, text = "Uzraksti burtu un es to aizšifrēšu")
label.pack()


# def sifresana():
#     sifr_burts = burts
#     label.config(text=f"Šifrētais burts ir: {sifr_burts.lower()}")
# # def decryption():
# #     cipher_text = user_text.get()
# #     plain_text = ""
# #     key = 3
# #     for i in range(len(cipher_text)):
# #         letter = cipher_text[i]
# #         if(letter.isupper()):
# #             plain_text+=chr((ord(letter)-key-65)%26+65)
# #         else:
# #             plain_text+=chr((ord(letter)-key-97)%26+97) 
# #     label4 =tk.Label(root,text=plain_text,width=20,bg="light yellow")
# #     label4.config()





# burts = "aābcčdeēfgģhiījkķlļmnņoprsštuūvzž"
burts = ["a","ā","b","c","č","d","e","ē","f","g","ģ","h","i","ī","j","k","ķ","l","ļ","m","n","ņ","o","p","r","s","š","t","u","ū","v","z","ž"]
def encryption():
    plain_text = ievade.get() 
    cipher_text = ""
    key = 3
    virziens = tk.Label(root, text = "Ievadi virzienu - šifrēt vai atšifrēt")
    virziens.pack()
    if virziens == "a":
        key = -key
    jaunais_teksts = ""
    for i in range(len(plain_text)):
        letter = plain_text[i]
        if letter in burts:
            index = burts.index(letter)
            new_index = (index + key) % len(burts)
            cipher_text += burts[new_index]
        else:
            cipher_text += letter 


        if burts in plain_text:
            i = burts.index[(i+key) % len(burts)]
            jaunais_teksts +=burts
        else:
            jaunais_teksts += burts
    return jaunais_teksts
        
           

    label3 = tk.Label(root, text=f"Šifrētais burts ir: {cipher_text}", width=40)
    label3.pack()


ievade = tk.Entry(root)
ievade.pack(pady=10)
ievade2 = tk.Entry(root)
ievade2.pack(pady=10)
button = tk.Button(root, text="Aizšifrēt", command=encryption)
button.pack()
button2 = tk.Button(root, text="Atšifrēt", command=encryption)
button2.pack()

root.geometry("400x300")
root.mainloop()






import tkinter as tk


burti = ["a", "ā", "b", "c", "č", "d", "e", "ē", "f", "g", "ģ", "h", "i", "ī", "j", "k", "ķ", "l", "ļ", "m", "n", "ņ", "o", "p", "r", "s", "š", "t", "u", "ū", "v", "z", "ž"]

def sifresana():
    plain_text = ievade1.get().lower()
    try:
        key = int(ievade2.get())
    except ValueError:
        label3.config(text="Lūdzu, ievadiet skaitli otrajā laukā!")
        return
    
    cipher_text = ""
    for letter in plain_text:
        if letter in burti:
            index = burti.index(letter)
            new_index = (index + key) % len(burti)
            cipher_text += burti[new_index]
        else:
            cipher_text += letter
    
    label3.config(text=f"Šifrēts teksts: {cipher_text}")


root = tk.Tk()
root.title("Šifrēšana")
root.geometry("400x300")

label = tk.Label(root, text="Ievadiet vārdu un nobīdi:")
label.pack()

ievade1 = tk.Entry(root)
ievade1.pack(pady=5)

ievade2 = tk.Entry(root)
ievade2.pack(pady=5)

button = tk.Button(root, text="Šifrēt", command=sifresana)
button.pack(pady=5)

label3 = tk.Label(root, text="")
label3.pack()

root.mainloop()

