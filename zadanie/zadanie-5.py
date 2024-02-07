#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

class RadioButtonApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Меню")

        self.label_result = tk.Label(root, text="Выберите блюдо", font=("Arial", 14))
        self.label_result.pack(pady=20)

        # Создаем переменную для хранения выбранной опции
        self.selected_option = tk.StringVar()

        # Создаем группу радиокнопок с выключенным индикатором
        options = ["Котлета", "Суп", "Гречка"]
        for option_text in options:
            radio_button = tk.Radiobutton(
                root,
                text=option_text,
                variable=self.selected_option,
                value=option_text,
                indicatoron=0,  # Выключенный индикатор
                command=self.update_label
            )
            radio_button.pack(pady=3)

    def update_label(self):
        selected_value = self.selected_option.get()
        self.label_result.config(text=f"Выбранное блюдо: {selected_value}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RadioButtonApp(root)
    root.mainloop()
