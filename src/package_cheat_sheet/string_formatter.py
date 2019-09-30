import re
import stringcase
import unicodedata


class StringFormatter:

    @classmethod
    def format_elements_to_snakecase(cls, a_list, internal_index=None):
        if internal_index is None:
            for counter in range(len(a_list)):
                a_list[counter] = cls.format_to_snakecase(a_list[counter])
        else:
            for element in a_list:
                element[internal_index] = cls.format_to_snakecase(element[internal_index])

    @classmethod
    def format_to_snakecase(cls, string):
        normalized_str = unicodedata.normalize('NFKD', string).encode('ASCII', 'ignore').decode()
        normalized_str = re.sub(r'[^a-zA-Z0-9]+', ' ', normalized_str)
        normalized_str = normalized_str.strip()
        normalized_str = normalized_str.lower() if (' ' in normalized_str) or (normalized_str.isupper()) \
            else stringcase.camelcase(normalized_str)  # FooBarBaz => fooBarBaz

        return stringcase.snakecase(normalized_str)  # foo-bar-baz => foo_bar_baz
