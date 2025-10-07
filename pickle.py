from tkinter import *
from tkinter import messagebox
import pickle

root = Tk()
root.geometry("300x500")
root.title("Войти в систему")


def registration():
    text = Label(text="Для входа в систему зарегистрируйтесь")
    text_log = Label(text="Введите ваш логин:")
    registr_login = Entry()
    text_password1 = Label(text="Введите ваш пароль")
    registr_password1 = Entry()
    text_password2 = Label(text="Еще раз пароль:")
    registr_password2 = Entry(show="*")
    button_registr = Button(text="Зарегистрироваться", command=lambda: save())

    def save():
        login_pass_save = {}
        login_pass_save[registr_login.get()] = registr_password1.get()
        f = open("login.txt", "wb")
        pickle.dump(login_pass_save, f)
        f.close()
        login()

    text.pack()
    text_log.pack()
    registr_login.pack()
    text_password1.pack()
    registr_password1.pack()
    text_password2.pack()
    registr_password2.pack()
    button_registr.pack()

def login():
    text_log = Label(text = "Поздравляем! Теперь вы можете войти в систему.")
    text_enter_login = Label(text = "Введите ваш логин")
    enter_login = Entry()
    text_enter_pass = Label(text = "Введите ваш пароль")
    enter_pass = Entry(show = "*")
    button_enter = Button(text = "Войти", command=lambda: log_pass())

    def log_pass():
        f = open("login.txt", "rb")
        a = pickle.load(f)
        f.close()
        if enter_login.get() in a:
            if enter_pass.get() == a[enter_login.get()]:
                messagebox.showinfo("Вход выполнен.", "Привет! У тебя 5 новых сообщений")
            else:
                messagebox.showerror("Ошибка", "Вы ввели неверный логин или пароль")
        else:
            messagebox.showerror("Ошибка!", "Неверный логин")
    text_log.pack()
    text_enter_login.pack()
    enter_login.pack()
    text_enter_pass.pack()
    enter_pass.pack()
    button_enter.pack()


registration()
root.mainloop()
