import tkinter as tk
from random import randint

BG_COLOR = "#222222"
FG_COLOR = "#FFFFFF"


def generate_numbers():
    fret = randint(0, 12)
    string = randint(1, 6)
    fret_label.config(text="Fret: " + str(fret), highlightbackground=BG_COLOR)
    string_label.config(text="String: " + str(string),
                        highlightbackground=BG_COLOR)


def repeat():
    generate_numbers()


root = tk.Tk()
root.title("Random Note Generator")

root.configure(bg=BG_COLOR)

font_style = ("TkDefaultFont", 30)
label_kwargs = {"font": font_style, "fg": FG_COLOR, "bg": BG_COLOR}

fret_label = tk.Label(root, text="Fret: ", **label_kwargs)
fret_label.pack()

string_label = tk.Label(root, text="String: ", **label_kwargs)
string_label.pack()

generate_button = tk.Button(
    root, text="Generate", command=generate_numbers, bg=BG_COLOR, fg=FG_COLOR, font=font_style)
generate_button.pack()

for child in root.winfo_children():
    if isinstance(child, tk.Frame):
        child.configure(bg=BG_COLOR)

root.after(1000, repeat)
root.mainloop()
