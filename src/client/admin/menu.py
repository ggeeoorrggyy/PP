import tkinter as tk
from tkinter import ttk
from tkinter import END
from src.client.admin.add import AddMenu
from src.client.admin.update import UpdMenu
from src.client.admin.delete import DelMenu
from src.client.api.resolvers import data_for_table_masters


class Menu(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Hello admin!")
        self.font = ('Times New Roman', 16)
        btn_add = tk.Button(self, text="Нанять мастера", font=("Times New Roman", 11), command=self.open_add_menu)
        btn_upd = tk.Button(self, text="Обновить мастера", font=("Times New Roman", 11), command=self.open_upd_menu)
        btn_del = tk.Button(self, text="Удалить мастера", font=("Times New Roman", 11), command=self.open_del_menu)
        btn_exit = tk.Button(self, text="Выйти из аккаунта", font=("Times New Roman", 11), command=exit)
        columns = ("id", "name_master", "type_of_service_id")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("id", text="ID")
        self.tree.heading("name_master", text="Имя")
        self.tree.heading("type_of_service_id", text="Тип сервиса")
        self.table_masters()
        self.tree.grid(row=0, column=0, rowspan=6, pady=10, padx=10)
        btn_add.grid(row=1, column=1, padx=2)
        btn_upd.grid(row=2, column=1, padx=2)
        btn_del.grid(row=3, column=1, padx=2)
        btn_exit.grid(row=4, column=1, padx=2)

    def table_masters(self):
        self.tree.delete(*self.tree.get_children())
        data_masters = data_for_table_masters()
        for master in data_masters:
            self.tree.insert("", END, values=master)

    def open_add_menu(self):
        self.table_masters()
        return AddMenu(self)

    def open_upd_menu(self):
        self.table_masters()
        return UpdMenu(self)

    def open_del_menu(self):
        self.table_masters()
        return DelMenu(self)