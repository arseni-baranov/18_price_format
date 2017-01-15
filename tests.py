import unittest
import format_price


class PriceFormatTestCase(unittest.TestCase):
    def test_negative_price(self):
        whole, fractional = format_price.format_price('-123.00545')
        self.assertEqual(whole, 'Ошибка - цена отрицательная')
        self.assertIsNone(fractional)

    def test_alpha_string_price(self):
        whole, fractional = format_price.format_price('123.0f564')
        self.assertEqual(whole, 'Ошибка - цена содержит буквы')
        self.assertIsNone(fractional)

    def test_replace_comma(self):
        whole, fractional = format_price.format_price('987,304654')
        self.assertEqual(whole, '987')
        self.assertEqual(fractional, '30')

    def test_incorrect_price(self):
        whole, fractional = format_price.format_price('123,123,00654')
        self.assertEqual(whole, 'Ошибка - неверная цена')
        self.assertIsNone(fractional)

    def test_correct_price(self):
        whole, fractional = format_price.format_price('123.4545')
        self.assertEqual(whole, '123')
        self.assertEqual(fractional, '45')


if __name__ == '__main__':
    unittest.main()
