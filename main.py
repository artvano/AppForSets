import customtkinter as ctk
from sets_functions import (
    check_univers, union, 
    intersection, diff, 
    symmetric_diff, addition, 
    subsets, size_of_set
)


class SetsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("App for sets")
        self.geometry("800x600")

        self.sets = {
            "U": [],
            "A": [],
            "B": [],
        }
        self.current_step = 0

        self._create_widgets()

    def _create_widgets(self):
        self.label_U = ctk.CTkLabel(
            self,
            text="Введите элементы универсального множества через запятую",
        )
        self.label_U.pack()

        self.entry_U = ctk.CTkEntry(self)
        self.entry_U.pack()

        self.button_U = ctk.CTkButton(
            self,
            text="Далее",
            width=30,
            height=10,
            command=self.next_step,
        )
        self.button_U.pack()

        self.label_A = ctk.CTkLabel(
            self,
            text="Введите элементы множества A через запятую",
        )
        self.entry_A = ctk.CTkEntry(self)
        self.button_A = ctk.CTkButton(
            self,
            text="Далее",
            width=30,
            height=10,
            command=self.next_step,
        )

        self.label_B = ctk.CTkLabel(
            self,
            text="Введите элементы множества B через запятую",
        )
        self.entry_B = ctk.CTkEntry(self)
        self.button_B = ctk.CTkButton(
            self,
            text="Подтвердить",
            width=30,
            height=10,
            command=self.next_step,
        )



    @staticmethod
    def _read_values(entry):
        return list(map(int, entry.get().split(", ")))

    def next_step(self):
        if self.current_step == 0:
            self.sets["U"] = self._read_values(self.entry_U)
            self.current_step += 1

            self.label_A.pack()
            self.entry_A.pack()
            self.button_A.pack()

        elif self.current_step == 1:
            self.sets["A"] = self._read_values(self.entry_A)
            self.current_step += 1

            self.label_B.pack()
            self.entry_B.pack()
            self.button_B.pack()

        elif self.current_step == 2:
            self.sets["B"] = self._read_values(self.entry_B)
            self.current_step += 1

            self.sets_label = ctk.CTkLabel(self, text="")
            self.sets_label.pack()
                
            self.message_label = ctk.CTkLabel(self, text="")
            self.message_label.pack()
                
            self.finish_input()
            self.current_step += 1


    def finish_input(self):
        changes = check_univers(
            self.sets["A"],
            self.sets["B"],
            self.sets["U"]
        )

        self.sets_label.configure(
            text=f"\nU = {self.sets['U']}\n"
            f"A = {self.sets['A']}\n"
            f"B = {self.sets['B']}"
        )

        messages = []

        if not changes["flag_for_A"]:
            messages.append("Множество A изменено: удалены элементы, которых нет в U.")
        if not changes["flag_for_B"]:
            messages.append("Множество B изменено: удалены элементы, которых нет в U.")

        self.message_label.configure(
            text = "\n".join(messages) if messages else "Множества A и B не были изменены"
        )

if __name__ == "__main__":
    app = SetsApp()
    app.mainloop()