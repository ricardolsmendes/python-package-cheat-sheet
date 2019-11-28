import unittest

import package_cheat_sheet


class StringFormatterTest(unittest.TestCase):

    def test_format_elements_snakecase_list(self):
        test_list = ['AA-AA', 'BB-BB']
        package_cheat_sheet.StringFormatter.format_elements_to_snakecase(test_list)
        self.assertListEqual(['aa_aa', 'bb_bb'], test_list)

    def test_format_elements_snakecase_internal_index(self):
        test_list = [['AA-AA', 'Test A'], ['BB-BB', 'Test B']]
        package_cheat_sheet.StringFormatter.format_elements_to_snakecase(
            test_list, internal_index=0)
        self.assertListEqual([['aa_aa', 'Test A'], ['bb_bb', 'Test B']], test_list)

    def test_format_string_to_snakecase_abbreviation(self):
        self.assertEqual('aaa', package_cheat_sheet.StringFormatter.format_to_snakecase('AAA'))
        self.assertEqual(
            'aaa_aaa', package_cheat_sheet.StringFormatter.format_to_snakecase('AAA-AAA'))

    def test_format_string_to_snakecase_camelcase(self):
        self.assertEqual(
            'camel_case', package_cheat_sheet.StringFormatter.format_to_snakecase('camelCase'))

    def test_format_string_to_snakecase_leading_number(self):
        self.assertEqual(
            '1_number', package_cheat_sheet.StringFormatter.format_to_snakecase('1 number'))

    def test_format_string_to_snakecase_repeated_special_chars(self):
        self.assertEqual(
            'repeated_special_chars',
            package_cheat_sheet.StringFormatter.format_to_snakecase('repeated   special___chars'))

    def test_format_string_to_snakecase_whitespaces(self):
        self.assertEqual(
            'no_leading_and_trailing',
            package_cheat_sheet.StringFormatter.format_to_snakecase(' no leading and trailing '))
        self.assertEqual(
            'no_leading_and_trailing',
            package_cheat_sheet.StringFormatter.format_to_snakecase('\nno leading and trailing\t'))

    def test_format_string_to_snakecase_special_chars(self):
        self.assertEqual(
            'special_chars',
            package_cheat_sheet.StringFormatter.format_to_snakecase('special!#@-_ chars'))
        self.assertEqual(
            'special_chars',
            package_cheat_sheet.StringFormatter.format_to_snakecase('! special chars ?'))

    def test_format_string_to_snakecase_unicode(self):
        self.assertEqual(
            'a_a_e_o_u', package_cheat_sheet.StringFormatter.format_to_snakecase(u'å ä ß é ö ü'))

    def test_format_string_to_snakecase_uppercase(self):
        self.assertEqual(
            'uppercase', package_cheat_sheet.StringFormatter.format_to_snakecase('UPPERCASE'))
        self.assertEqual(
            'upper_case', package_cheat_sheet.StringFormatter.format_to_snakecase('UPPER CASE'))
