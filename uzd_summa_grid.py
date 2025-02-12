import tkinter as tk

root = tk.Tk()
root.title("Summa")

label = tk.Label(root, text = "Ievadi ciparus un nospied uz pogu!")
label.pack()


def summa_text():
  try:
    sk1 = float(ievade1.get())
    sk2 = float(ievade2.get())
    label.config(text=f"Summa ir: {sk1+sk2}")
  except ValueError:
    label.config(text=f"Ievadiet ciparus")
def starpiba_text():
  try:
    sk1 = float(ievade1.get())
    sk2 = float(ievade2.get())
    label.config(text=f"Starpība ir: {sk1-sk2}")
  except ValueError:
    label.config(text=f"Ievadiet ciparus")
def reizinasana_text():
  try:
    sk1 = float(ievade1.get())
    sk2 = float(ievade2.get())
    label.config(text=f"Reizināšana ir: {sk1*sk2}")
  except ValueError:
    label.config(text=f"Ievadiet ciparus")
def dalisana_text():
  try:
    sk1 = float(ievade1.get())
    sk2 = float(ievade2.get())
    label.config(text=f"Starpība ir: {sk1/sk2}")
  except ZeroDivisionError:
    label.config(text="Ar nulli dalīt nedrīkst!")
    # if sk2 == 0:
    #   label.config(text="Ar nulli dalīt nedrīkst")
    # else:
    #   label.config(text=f"Reizināšana ir: {sk1/sk2}")
    
  

def clear_text():
    ievade1.delete(0, tk.END)
    ievade2.delete(0, tk.END)
    label.config(text="Ievadiet skaitļus")

ievade1 = tk.Entry(root) #ievade Logs
ievade1.pack(pady=10)
ievade2 = tk.Entry(root) #ievade Logs
ievade2.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack()
button = tk.Button(button_frame, text= "+", command= summa_text) 
button.grid(row=0, column=0, padx=5)
button = tk.Button(button_frame, text= "-", command= starpiba_text) 
button.grid(row=0, column=1, padx=5)
button = tk.Button(button_frame, text= "*", command= reizinasana_text) 
button.grid(row=0, column=2, padx=5)
button = tk.Button(button_frame, text= "/", command= dalisana_text) 
button.grid(row=0, column=3, padx=5)
button = tk.Button(button_frame,text= "Dzēst", command= clear_text) 
button.grid(row=0, column=4, pady=5)
root.geometry("400x300")

root.mainloop()
