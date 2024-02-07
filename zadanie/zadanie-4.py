#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog

class FileIOApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Программа для работы с файлами")

        # Создаем однострочное текстовое поле для ввода имени файла
        self.filename_entry = tk.Entry(root)
        self.filename_entry.pack(pady=10)

        # Создаем многострочное текстовое поле для отображения и редактирования содержимого файла
        self.text_area = tk.Text(root, height=15, width=50)
        self.text_area.pack(pady=10)

        # Кнопка "Открыть" для чтения файла
        open_button = tk.Button(root, text="Открыть", command=self.open_file)
        open_button.pack(pady=3)

        # Кнопка "Сохранить" для записи файла
        save_button = tk.Button(root, text="Сохранить", command=self.save_file)
        save_button.pack(pady=3)

    def open_file(self):
        file_path = filedialog.askopenfilename(initialdir="./", title="Выберите файл")
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, content)
            self.filename_entry.delete(0, tk.END)
            self.filename_entry.insert(0, file_path)

    def save_file(self):
        file_path = self.filename_entry.get()
        content = self.text_area.get(1.0, tk.END)
        with open(file_path, "w") as file:
            file.write(content)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileIOApp(root)
    root.mainloop()
