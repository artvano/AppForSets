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

        self.result_label = ctk.CTkLabel(self, text="")


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
            self.open_function_window()




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

    def open_function_window(self):
        self.function_window = ctk.CTkToplevel(self)
        self.function_window.title("Выбор функции")
        self.function_window.geometry("600x350")
        self.function_window.transient(self)
        self.function_window.lift()

        self.left_frame = ctk.CTkFrame(self.function_window)
        self.left_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(self.left_frame, text="Операции над одним множеством").pack(pady=10)

        ctk.CTkButton(
            self.left_frame,
            text="Дополнение A",
            command=lambda: self.show_result(
                "addition(A, U)",
                addition(self.sets["A"], self.sets["U"])
            )
        ).pack(pady=5)

        self.subsets_button = ctk.CTkButton(
            self.left_frame,
            text="Подмножества A",
            command=lambda: self.show_result("subsets(A)", subsets(self.sets["A"]))
        )
        self.subsets_button.pack(pady=5)

        self.size_button = ctk.CTkButton(
            self.left_frame,
            text="Мощность A",
            command=lambda: self.show_result(
                "size_of_set(A)", size_of_set(self.sets["A"])
            )
        )
        self.size_button.pack(pady=5)

        self.complement_b_button = ctk.CTkButton(
            self.left_frame,
            text="Дополнение B",
            command=lambda: self.show_result(
                "addition(B, U)",
                addition(self.sets["B"], self.sets["U"])
            )
        )
        self.complement_b_button.pack(pady=5)

        self.subsets_b_button = ctk.CTkButton(
            self.left_frame,
            text="Подмножества B",
            command=lambda: self.show_result(
                "subsets(B)", subsets(self.sets["B"])
            )
        )
        self.subsets_b_button.pack(pady=5)

        self.size_b_button = ctk.CTkButton(
            self.left_frame,
            text="Мощность B",
            command=lambda: self.show_result(
                "size_of_set(B)", size_of_set(self.sets["B"])
            )
        )
        self.size_b_button.pack(pady=5)

        self.right_frame = ctk.CTkFrame(self.function_window)
        self.right_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.right_label = ctk.CTkLabel(
            self.right_frame,
            text="Операции над двумя множествами"
        )
        self.right_label.pack(pady=10)

        self.union_button = ctk.CTkButton(
            self.right_frame,
            text="Объединение A и B",
            command=lambda: self.show_result(
                "union", union(self.sets["A"], self.sets["B"])
            )
        )
        self.union_button.pack(pady=5)

        self.intersection_button = ctk.CTkButton(
            self.right_frame,
            text="Пересечение A и B",
            command=lambda: self.show_result(
                "intersection", intersection(self.sets["A"], self.sets["B"])
            )
        )
        self.intersection_button.pack(pady=5)

        self.diff_button = ctk.CTkButton(
            self.right_frame,
            text="Разность A - B",
            command=lambda: self.show_result(
                "diff(A, B)", diff(self.sets["A"], self.sets["B"])
            )
        )
        self.diff_button.pack(pady=5)

        self.diff_b_a_button = ctk.CTkButton(
            self.right_frame,
            text="Разность B - A",
            command=lambda: self.show_result(
                "diff(B, A)", diff(self.sets["B"], self.sets["A"])
            )
        )
        self.diff_b_a_button.pack(pady=5)

        self.symmetric_diff_button = ctk.CTkButton(
            self.right_frame,
            text="Симметрическая разность",
            command=lambda: self.show_result(
                "symmetric_diff",
                symmetric_diff(self.sets["A"], self.sets["B"]),
            )
        )
        self.symmetric_diff_button.pack(pady=5)

    def show_result(self, function_name, result):
        self.result_label.configure(
            text=f"Функция: {function_name}\nРезультат: {result}"
        )
        self.result_label.pack(pady=10)


if __name__ == "__main__":
    app = SetsApp()
    app.mainloop()