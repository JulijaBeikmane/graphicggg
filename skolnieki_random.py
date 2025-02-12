import tkinter as tk
import random

root = tk.Tk()
root.title("RandomChoice")

label = tk.Label(root, text = "Uzspiež uz vēlamo klasi, lai izvelēties skolnieku randomā")
label.pack()

class_12b = ["Kristaps", "Enija", "Anna", "Leonīds", "Stepans"]
class_12a = ["Artūrs", "Marija", "Alīna", "Kristiāns"]
class_11a = ["Amanda", "Mārtiņš", "Elīne", "Laura"]

def pick_student12b():
    random_element1 = random.choice(class_12b)
    label.config(text=f"Tagad ies: {random_element1}")
def pick_student12a():
    random_element2 = random.choice(class_12a)
    label.config(text=f"Tagad ies: {random_element2}")
def pick_student11a():
    random_element3 = random.choice(class_11a)
    label.config(text=f"Tagad ies: {random_element3}")
def clear_text():
    ievade.delete(0, tk.END)
    label.config(text="Ievadiet skaitļus")


ievade = tk.Entry(root) #ievade Logs
ievade.pack(pady=10)

# button = tk.Button(root, text= "12b", command= summa_text) 
# button.pack(side="left", padx=5)

button_frame = tk.Frame(root)
button_frame.pack()
button = tk.Button(button_frame, text= "12b", command= pick_student12b) 
button.grid(row=0, column=0, padx=5)
button = tk.Button(button_frame, text= "12a", command= pick_student12a) 
button.grid(row=0, column=1, padx=5)
button = tk.Button(button_frame, text= "11a", command= pick_student11a) 
button.grid(row=0, column=2, padx=5)
button = tk.Button(button_frame, text= "Dzēst", command= clear_text) 
button.grid(row=0, column=3, padx=5)

root.geometry("400x300")
root.mainloop()
