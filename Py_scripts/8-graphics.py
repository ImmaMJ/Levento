import numpy as np
import matplotlib.pyplot as plt

# загрузка данных из файлов
time = np.loadtxt('time.txt')
voltage = np.loadtxt('voltage.txt')

# создание объектов Figure и Axes
fig, ax = plt.subplots()

# построение графика
ax.plot(time, voltage, color='blue', linestyle='-', marker='o', markersize=3, markevery=100, label='Зависимость напряжения от времени')

# расчет максимальных и минимальных значений для шкалы
x_min, x_max = np.min(time), np.max(time)
y_min, y_max = np.floor(np.min(voltage)), np.ceil(np.max(voltage))

# задание максимальных и минимальных значений для шкалы
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)

# задание подписей x и y осей
ax.set_xlabel('Время, с')
ax.set_ylabel('Напряжение, В')

# задание названия графика
title = 'График зависимости напряжения от времени'
ax.set_title(title, loc='center', wrap=True)

# настройка сетки
ax.grid(color='gray', linestyle='--', linewidth=0.5)
ax.minorticks_on()
ax.grid(which='minor', color='gray', linestyle=':', linewidth=0.5)

# нанесение текста
text = f'Максимальное напряжение: {y_max} В\nМинимальное напряжение: {y_min} В'
x_pos = x_min + (x_max - x_min) * 0.05
y_pos = y_min + (y_max - y_min) * 0.9
ax.text(x_pos, y_pos, text, fontsize=10, color='black')

# отображение легенды
ax.legend()

# отображение графика
plt.show()
