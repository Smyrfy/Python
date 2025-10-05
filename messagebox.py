from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("300x200")

def clear_root():
    for widget in root.winfo_children():
        widget.destroy()

def que_one():
    clear_root()
    question = Label(root, text="Висит груша, и её нельзя скушать?")
    answer = Entry()
    btn = Button(root, text="Ответить", command=lambda: game1(answer.get()))
    question.grid(pady=10)
    answer.grid(pady=5)
    btn.grid(pady=5)

def game1(ans):
    if ans.lower() == "лампочка":
        que_two()
    else:
        messagebox.showerror("Ошибка", "Попробуй еще раз")

def que_two():
    clear_root()
    question_2 = Label(root, text="Зимой и летом одного цвета?")
    answer_2 = Entry()
    btn_2 = Button(root, text="Ответить", command=lambda: game2(answer_2.get()))
    question_2.grid(pady=10)
    answer_2.grid(pady=5)
    btn_2.grid(pady=5)

def game2(ans):
    if ans.lower() == "ёлка":
        messagebox.showinfo("Победа", "Ты молодец!")
    else:
        messagebox.showerror("Ошибка", "Попробуй еще раз")

que_one()
root.mainloop()
