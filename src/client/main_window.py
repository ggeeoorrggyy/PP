import tkinter as tk
import tkinter.messagebox

from src.client.api.resolvers import check_login
from src.client.admin.menu import Menu


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.username = tk.StringVar()
        self.user_password = tk.StringVar()
        self.font = ('Times New Roman', 16)

        lbl_main = tk.Label(self, text="Вход в систему", font=self.font)
        lbl_login = tk.Label(self, text="Логин", font=self.font)
        lbl_pass = tk.Label(self, text='Пароль', font=self.font)
        entry_login = tk.Entry(self, font=self.font, textvariable=self.username)
        entry_pass = tk.Entry(self, font=self.font, textvariable=self.user_password)
        btn_enter = tk.Button(self, text='Вход', font=self.font, command=self.open_menu)
        btn_close = tk.Button(self, text='Отмена', font=self.font, command=exit)

        lbl_main.grid(row=0, columnspan=2, column=1)
        lbl_login.grid(row=1, column=0, pady=10, ipadx=10)
        entry_login.grid(row=1, column=1, columnspan=3, padx=30, pady=10)
        lbl_pass.grid(row=2, column=0, pady=10, ipadx=10)
        entry_pass.grid(row=2, column=1, columnspan=3, padx=30, pady=10)
        btn_enter.grid(row=3, column=1, pady=10)
        btn_close.grid(row=3, column=2, pady=10)

    def checking_login(self):
        self.grab_set()
        post = check_login(login=self.username.get(),
                           password=self.user_password.get())
        return post

    def checking_post(self) -> Menu | None:
        power_level = self.checking_login()
        match power_level:
            case 1: return Menu(self)
            case 2: return Menu(self)
            case 3: return Menu(self)
            case _: return None

    def open_menu(self):
        if type(self.checking_login()) == int:
            self.withdraw()
            self.checking_post()
        else:
            tk.messagebox.showerror(title="Wrong login",
                                    message="Логин или пароль не верны")