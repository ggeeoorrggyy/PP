import tkinter as tk
from src.client.api.resolvers import new_master
import tkinter.messagebox


class AddMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add master")
        self.name = tk.StringVar()
        self.type_id = tk.IntVar()
        self.font = ('Times New Roman', 16)

        lbl_main = tk.Label(self, text="Добавление мастера\n", font=("Times New Roman", 20))
        lbl_name = tk.Label(self, text="       name", font=self.font)
        lbl_type_id = tk.Label(self, text="service ID", font=("Times New Roman", 14))
        entry_name = tk.Entry(self, textvariable=self.name, font=self.font)
        entry_type_id = tk.Entry(self, textvariable=self.type_id, font=self.font)
        btn_back = tk.Button(self, text="Отмена", font=self.font, command=self.destroy)
        btn_enter = tk.Button(self, text="Ок", font=self.font, command=self.add_master)

        lbl_main.grid(row=0, columnspan=3, column=0)
        lbl_name.grid(row=1, column=0, pady=10, padx=30)
        entry_name.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        lbl_type_id.grid(row=2, column=0, pady=10, ipadx=10)
        entry_type_id.grid(row=2, column=1, columnspan=3, padx=30, pady=10)
        btn_back.grid(row=3, column=0, columnspan=2, pady=10)
        btn_enter.grid(row=3, column=2, pady=10)

    def add_master(self):
        self.grab_set()
        answer = new_master(name=self.name.get(), id=self.type_id.get())
        if answer["code"] == 200:
            self.destroy()
            tkinter.messagebox.showinfo(title="Successfully",
                                        message="Успех!")
        else:
            tkinter.messagebox.showerror(title="Error",
                                    message="Ошибка!")