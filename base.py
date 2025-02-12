import tkinter as tk

root = tk.Tk()
root.title("Mans pirmais logs")

def show_text():
  label.config(text=f"Tu ievadīji: {ievade.get()}")
  
# message = tk.Label(root, text="Hello!") #etiķetes
# message.pack()

ievade = tk.Entry(root) #ievade Logs
ievade.pack()

button = tk.Button(root, text= "Press me!", command= show_text) #poga
button.pack()

label = tk.Label(root, text = "Ievadi tekstu un nospied uz pogu!")
label.pack()

root.geometry("300x200")
root.mainloop()
