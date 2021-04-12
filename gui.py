from tkinter import *
from tkinter.filedialog import asksaveasfilename

from PIL import Image, ImageTk
import bot
import user

root = Tk()
root.title("Chat Bot")
root.geometry("500x560")
root.resizable(width=FALSE, height=FALSE)

list_history_message = []


def convert_list_to_string(list):
    string = " "
    return string.join(list)


def click_button1():
    text_all = "\n" + user.send_good_bay() + "\n" + bot.answer_good_bay() + "\n" + "---------------"
    list_history_message.append(text_all)
    text.configure(text=convert_list_to_string(list_history_message))


def click_button2():
    text_all = "\n" + user.send_question() + "\n" + bot.answer_question() + "\n" + bot.send_question() + "\n" + "--------------- "
    list_history_message.append(text_all)
    text.configure(text=convert_list_to_string(list_history_message))


def click_button3():
    text_all = "\n" + user.send_answer() + "\n" + "---------------"
    list_history_message.append(text_all)
    text.configure(text=convert_list_to_string(list_history_message))


def click_button4():
    text_all = "\n" + user.send_welcome() + "\n" + bot.answer_welcome() + "\n" + "---------------"
    list_history_message.append(text_all)
    text.configure(text=convert_list_to_string(list_history_message))


def clear_chat():
    list_history_message.clear()
    text.configure(text=convert_list_to_string(list_history_message))


def save_file():
    filename = asksaveasfilename(filetypes=[("Plik tekstowy", "*.txt")],
                                 defaultextension="*.txt")
    if filename:
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(convert_list_to_string(list_history_message))


text = Label(root, text="Naciśnij jeden z przycisków\naby porozmawiać z Botem!", width=30, height=560, bg="white",
             anchor=SW,
             justify=LEFT)
text.config(font=("Arial", 14))
text.pack(side=LEFT)

button_exit = Button(root, text="Wyjdź z programu", width=167, height=5, command=root.quit)
button_exit.pack(side=BOTTOM)

button_welcome = Button(root, text="Pożegnaj się", width=167, height=5, command=click_button1)
button_welcome.pack(side=BOTTOM)

button_question = Button(root, text="Zadaj pytanie", width=167, height=5, command=click_button2)
button_question.pack(side=BOTTOM)

button_answer_click = Button(root, text="Odpowiedz", width=167, height=5, command=click_button3)
button_answer_click.pack(side=BOTTOM)

button_good_bay = Button(root, text="Przywitaj się", width=167, height=5, command=click_button4)
button_good_bay.pack(side=BOTTOM)

logo = ImageTk.PhotoImage(Image.open("logo.jpg"))
logo_label = Label(image=logo)
logo_label.pack(side=BOTTOM)

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Chat", command=clear_chat)
file_menu.add_command(label="Save As..", command=save_file)
file_menu.add_command(label="Exit..", command=root.quit)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Clear Chat", command=clear_chat)

root.mainloop()
