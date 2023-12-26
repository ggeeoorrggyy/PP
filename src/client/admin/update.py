import tkinter as tk
from src.client.api.resolvers import upd_master
import tkinter.messagebox


class UpdMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Update master")
        self.id = tk.IntVar()
        self.name = tk.StringVar()
        self.service_id = tk.IntVar()
        self.font = ('Times New Roman', 16)

        lbl_main = tk.Label(self, text="Обновление мастера\n", font=("Times New Roman", 20))
        lbl_id = tk.Label(self, text="            ID", font=self.font)
        lbl_name = tk.Label(self, text="        name", font=self.font)
        lbl_service_id = tk.Label(self, text="service ID", font=("Times New Roman", 14))
        entry_id = tk.Entry(self, textvariable=self.id, font=self.font)
        entry_name = tk.Entry(self, textvariable=self.name, font=self.font)
        entry_service_id = tk.Entry(self, textvariable=self.service_id, font=self.font)
        btn_back = tk.Button(self, text="Отмена", font=self.font, command=self.destroy)
        btn_enter = tk.Button(self, text="Ок", font=self.font, command=self.upd_master)

        lbl_main.grid(row=0, columnspan=3, column=0)
        lbl_id.grid(row=1, column=0)
        entry_id.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        lbl_name.grid(row=2, column=0, pady=10, padx=30)
        entry_name.grid(row=2, column=1, columnspan=3, padx=30, pady=10)
        lbl_service_id.grid(row=3, column=0, pady=10, ipadx=10)
        entry_service_id.grid(row=3, column=1, columnspan=3, padx=30, pady=10)
        btn_back.grid(row=4, column=0, columnspan=2, pady=10)
        btn_enter.grid(row=4, column=2, pady=10)

    def upd_master(self):
        self.grab_set()
        answer = upd_master(id=self.id.get(), name=self.name.get(), type_id=self.service_id.get())
        if answer["code"] == 200:
            self.destroy()
            tkinter.messagebox.showinfo(title="Successfully",
                                        message="Мастер обновлен успешно")
        else:
            tkinter.messagebox.showerror(title="Wrong data",
                                         message="Данные для обновления мастера введены неверно!")