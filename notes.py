import tkinter as tk
from random import randint


def generate_numbers():
    fret = randint(0, 12)
    string = randint(1, 6)
    fret_label.config(text="Fret: " + str(fret))
    string_label.config(text="String: " + str(string))


def repeat():
    generate_numbers()


root = tk.Tk()
root.title("Random Note Generator")

fret_label = tk.Label(root, text="Fret: ")
fret_label.pack()

string_label = tk.Label(root, text="String: ")
string_label.pack()

generate_button = tk.Button(root, text="Generate", command=generate_numbers)
generate_button.pack()


root.after(1000, repeat)
root.mainloop()
