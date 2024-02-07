#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operator.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Ошибка"
        else:
            result = "Ошибка"

        label_result.config(text=result)
    except ValueError:
        label_result.config(text="Ошибка")

# Создаем основное окно
root = tk.Tk()
root.title("Калькулятор")

# Создаем текстовые поля и метку
entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, padx=10, pady=10)

entry2 = tk.Entry(root)
entry2.grid(row=0, column=1, padx=10, pady=10)

operator = tk.StringVar()
operator.set('+')

# Создаем кнопки операций
add_button = tk.Radiobutton(root, text="+", variable=operator, value='+')
add_button.grid(row=1, column=0)

subtract_button = tk.Radiobutton(root, text="-", variable=operator, value='-')
subtract_button.grid(row=1, column=1)

multiply_button = tk.Radiobutton(root, text="*", variable=operator, value='*')
multiply_button.grid(row=2, column=0)

divide_button = tk.Radiobutton(root, text="/", variable=operator, value='/')
divide_button.grid(row=2, column=1)

# Создаем кнопку для вычисления
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=4, pady=5)

# Метка для отображения результата
label_result = tk.Label(root, text="")
label_result.grid(row=4, column=0, columnspan=4)

# Запускаем главный цикл
root.mainloop()
