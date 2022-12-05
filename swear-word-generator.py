import tkinter
import random
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  
app.geometry("500x300")

def button_function():
    print(random.choice(first)+random.choice(second)+random.choice(third), sep="")

    label.configure(text=random.choice(first) + random.choice(second) + random.choice(third))


label = customtkinter.CTkLabel(master=app, text="Нажми на кнопку", width=120, height=55, corner_radius=20)
label.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app, text="сгенерировать", command=button_function)
button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)


first = ["пиздо", "хуе", "ахуе", "ебнуто", "дохуя", "пере", "срако", "жопо", "ебле", "бляди"] #приставка
second = ["ёбо", "пиздо", "хуе", "чмоне","блудо", "вагино", "гомо", "пердуно", "", "" ] #основная часть слова
third = ["блядский", "хуев", "стый", "глист", "головый", "дрочила", "вошка"] #окончание


app.mainloop()
