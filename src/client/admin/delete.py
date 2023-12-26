import tkinter as tk
from src.client.api.resolvers import del_master
import tkinter.messagebox


class DelMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Delete master")
        self.id = tk.IntVar()
        self.font = ('Times New Roman', 16)

        lbl_main = tk.Label(self, text="Удаление мастера", font=("Times New Roman", 20))
        lbl_id = tk.Label(self, text="ID", font=self.font)
        entry_id = tk.Entry(self, textvariable=self.id, font=self.font)
        btn_back = tk.Button(self, text="Отмена", font=self.font, command=self.destroy)
        btn_enter = tk.Button(self, text="Ок", font=self.font, command=self.upd_channel)

        lbl_main.grid(row=0, columnspan=3, column=0, padx=20, ipadx=10, ipady=10)
        lbl_id.grid(row=1, column=0, padx=20, ipadx=10, ipady=10)
        entry_id.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        btn_back.grid(row=4, column=0, columnspan=2, pady=10)
        btn_enter.grid(row=4, column=2, pady=10)

    def upd_channel(self):
        self.grab_set()
        answer = del_master(id=self.id.get())
        if answer["code"] == 200:
            self.destroy()
            tkinter.messagebox.showinfo(title="Successfully",
                                        message="Мастер удален успешно")
        else:
            tkinter.messagebox.showerror(title="Wrong data",
                                         message="Данные для удаления мастера введены неверно!")