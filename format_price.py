import argparse
import re


def get_console_arguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [аргументы]',
                                     description='Форматирование цены с помощью %(prog)s')
    parser.add_argument('-p', '--price', help='Цена товара')
    return parser


def check_letters(price):
    return bool(re.search(r'[а-яА-Яa-zA-zёЁ]', price))


def check_special_chars(price):
    return bool(re.search(r'[^а-яА-Яa-zA-zёЁ0-9.,]', price))


def check_negative_numbers(price):
    return bool(price.startswith('-'))


def split_float_number(price):
    whole, fraction = '{:,.2f}'.format(price).split('.')
    return whole.replace(',', ' '), fraction


def format_price(price):
    if check_letters(price):
        return 'Ошибка - цена содержит буквы', None
    elif check_negative_numbers(price):
        return 'Ошибка - цена отрицательная', None
    elif check_special_chars(price):
        return 'Ошибка - цена содержит спец. символы', None
    else:
        price = price.replace(',', '.')
        if price.count('.') == 1:
            return split_float_number(float(price))
        else:
            return 'Ошибка - неверная цена', None


def main():
    arguments = get_console_arguments().parse_args()
    price = arguments.price
    if price is None:
        price = input('Введите цену для форматирования: ')
    ready_price = format_price(price)
    print('.'.join(filter(None, ready_price)))

if __name__ == '__main__':
    main()
