import customtkinter as ctk
from sets_functions import(
    check_univers,
    union,
    intersection,
    diff,
    symmetric_diff,
    addition,
    subsets,
    size_of_set
)

sets = {
    "U": [],
    "A": [],
    "B": []
}
step = 0

def next_step():
    global step

    if step == 0:
        sets["U"] = list(map(int, _U.get().split(", ")))
        step += 1

        label_A.pack()
        _A.pack()
        button_A.pack()

    elif step == 1:
        sets["A"] = list(map(int, _A.get().split(", ")))
        step += 1

        label_B.pack()
        _B.pack()
        button_B.pack()

    elif step == 2:
        sets["B"] = list(map(int, _B.get().split(", ")))
        step += 1

        print(sets)


app = ctk.CTk()
app.title("App for sets")
app.geometry("800x600")

label_U = ctk.CTkLabel(app, text="Введите элементы универса через ','")
label_U.pack()
_U = ctk.CTkEntry(app)
_U.pack()

button_U = ctk.CTkButton(app, text="Далее", width=30, height=10, command=next_step)
button_U.pack()

label_A = ctk.CTkLabel(app, text="Введите элементы множества A через ', '")
_A = ctk.CTkEntry(app)
button_A = ctk.CTkButton(app, text="Далее", width=30, height=10, command=next_step)

label_B = ctk.CTkLabel(app, text="Введите элементы множества B через ', '")
_B = ctk.CTkEntry(app)
button_B = ctk.CTkButton(app, text="Подтвердить", width=30, height=10, command=next_step)

app.mainloop()