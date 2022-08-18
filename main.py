import tkinter as tk
from tkinter import ttk
from tkinter import *

# Root window
window = tk.Tk()
window.title('Yarn Weight')
window.geometry('400x200')

stitches = tk.StringVar()
weight = tk.StringVar()


def get_answer():
    stitches = int(label_answer.get())
    weight = "\n" + yarn_weight(stitches)
    output.config(state=NORMAL)
    output.delete(1.0, END)
    output.tag_config("center", justify="center")
    output.insert(tk.END, weight)
    output.tag_add("center", "1.0", "end")
    output.config(state=DISABLED)


# Text label
label_question = Label(window, text="How many stitches in 4inch/10cm?")
label_question.pack(padx=10, pady=10)
# Answer label
label_answer = ttk.Entry(window, textvariable=stitches)
label_answer.pack(padx=10, pady=10)
label_answer.focus()
# Show weight button
button = tk.Button(window, text="Show yarn weight", command=get_answer)
button.pack()
# Yarn Weight text / output
output = Text(window, height=3, width=40)
output.pack(padx=10, pady=10)


# function that decides the yarn weight
def yarn_weight(stitches):
    if stitches <= 6:
        return "Jumbo"
    elif 7 <= stitches <= 12:
        return "Super Bulky"
    elif stitches == 13:
        return "Between Super Bulky and Bulky"
    elif 14 <= stitches <= 15:
        return "Bulky"
    elif 16 <= stitches <= 17:
        return "Between Bulky and Aran"
    elif stitches == 18:
        return "Aran"
    elif stitches == 19:
        return "Between Aran and Worsted"
    elif stitches == 20:
        return "Worsted"
    elif stitches == 21:
        return "Between Worsted and DK"
    elif stitches == 22:
        return "DK"
    elif stitches == 23:
        return "Between DK and Sport"
    elif 24 <= stitches <= 26:
        return "Sport"
    elif stitches == 27:
        return "Between Sport and Fingering"
    elif stitches == 28:
        return "Fingering"
    elif 29 <= stitches <= 31:
        return "Between Fingering and Light Fingering"
    elif stitches == 32:
        return "Light Fingering"
    elif 33 <= stitches <= 34:
        return "Lace"
    else:
        return "Outside the range"


window.mainloop()

