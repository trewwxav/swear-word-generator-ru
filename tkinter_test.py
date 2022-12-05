import random
from tkinter import *

def test():
    print(random.choice(first)+random.choice(second)+random.choice(third), sep="")

    text_label.config(text=random.choice(first)+random.choice(second)+random.choice(third))

root = Tk()

root.title("swear word generator")
root.geometry("550x350")

button = Button(root, text="сгенерировать", font=40, command=test)
button.pack(side=BOTTOM, pady=100)


first = ["пиздо", "хуе", "ахуе", "ебнуто", "дохуя", "пере", "срако", "жопо", "ебле", "бляди"] #приставка
second = ["ёбо", "пиздо", "хуе", "чмоне","блудо", "вагино", "гомо", "пердуно", "", "" ] #основная часть слова
third = ["блядский", "хуев", "стый", "глист", "головый", "дрочила", "вошка"] #окончание

a = (random.choice(first)+random.choice(second)+random.choice(third))

text_label = Label(root, text="нажми на кнопку", font=40, pady=50)
text_label.pack()


root.mainloop()
