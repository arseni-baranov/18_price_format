# Форматирования цены

Данный скрипт получает из базы данных цену товара в виде строки "3245.000000" и приводит её к более наглядному виду "3 245.00".
У скрипта два интерфейса использования:

* Программный, для использования на сайте
* Command Line Interface (CLI) - для запуска в ручном режиме из консоли.

Код анализирует входные данные, и проверяет их корректность.
Если данные верны, то результатом работы будет кортеж с отформатированной ценой товара из целой и дробной частей.
В противном случае, строка с заглушкой '?'.

Чтобы проверить отработку некорректных данных написаны тесты для этой функции с использованием модуля Unittest.


## Руководство по применению

запустить скрипт:
```
python format_price.py -p 3245.000000
python tests.py
```
в результате мы получим отформатированную строку вида: 3 245.00
