from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

N = 8 # Число файлов исходных данных

# Лист, содержащий значения количества цитат для каждой из статей
citations = []

# Cчитывание данных из файлов:
for i in range(1, N, 1):

    # Открытие очередного файла исходных данных и считывание его содержимого:
    with open(str(i) + ".html", "r", encoding="UTF8") as f:

        # Получаем объект в виде "супа", содержащий страницу
        soup = BeautifulSoup(f.read(), 'lxml')

        # Выделяем из "супа" нужные нам элементы
        elements = list(map(lambda x: int(x.text),
            soup.find_all(name="td", attrs={"valign": "middle", "align": "center"})[8:]))

        print(elements)

        # Добавим в общий список данные из этого файла:
        citations += elements

# Получим из списка значений словарь вида "число цитирований - количество статей"
s = sorted(set(citations))
d = dict()
for el in s:
    d[el] = citations.count(el)

# Соответственно получаем списки для построения графика по точкам
x = d.keys()
y = d.values()

# Настраиваем график для удобного отображения
fig, ax = plt.subplots()
ax.plot(x, y)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(which='both', width=2)
ax.tick_params(which='major', length=7)
ax.tick_params(which='minor', length=4, color='black')
plt.xlabel('x - число ссылок')
plt.ylabel('y - количество работ')
plt.title('График о количестве работ с определенным количеством ссылок')
plt.xlim([0, max(x)+5])
plt.ylim([0, max(y)+5])
plt.xticks(np.arange(0, max(x)+5, 5))
plt.yticks(np.arange(0, max(y)+5, 5))

# Строим график
plt.show()


