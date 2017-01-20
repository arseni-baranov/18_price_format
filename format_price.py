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


def format_price(price, default_error="?"):
    if check_letters(price):
        return default_error, None
    elif check_negative_numbers(price):
        return default_error, None
    elif check_special_chars(price):
        return default_error, None
    else:
        price = price.replace(',', '.')
        if price.count('.') == 1:
            return split_float_number(float(price))
        else:
            return default_error, None


def main():
    arguments = get_console_arguments().parse_args()
    price = arguments.price
    if price is None:
        price = input('Введите цену для форматирования: ')
    ready_price = format_price(price)
    print('.'.join(filter(None, ready_price)))

if __name__ == '__main__':
    main()
