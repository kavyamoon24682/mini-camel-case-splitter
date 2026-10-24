import unittest

from mini_camel_case_splitter import split, split_camel_case
from mini_camel_case_splitter.core import split as core_split


class TestSplit(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split(""), [])

    def test_single_word_lowercase(self):
        self.assertEqual(split("hello"), ["hello"])

    def test_single_word_uppercase(self):
        self.assertEqual(split("HELLO"), ["hello"])

    def test_camel_case(self):
        self.assertEqual(split("camelCaseWords"), ["camel", "case", "words"])

    def test_pascal_case(self):
        self.assertEqual(split("PascalCaseWords"), ["pascal", "case", "words"])

    def test_acronym_before_lowercase_word(self):
        self.assertEqual(split("HTTPServer"), ["http", "server"])

    def test_acronym_before_uppercase_word(self):
        self.assertEqual(split("XMLParser"), ["xml", "parser"])

    def test_consecutive_acronyms(self):
        self.assertEqual(split("XMLHttpRequest"), ["xml", "http", "request"])

    def test_trailing_acronym(self):
        self.assertEqual(split("parseXML"), ["parse", "xml"])

    def test_digit_after_letter(self):
        self.assertEqual(split("file2Name"), ["file", "2", "name"])

    def test_letter_after_digit(self):
        self.assertEqual(split("version2Beta"), ["version", "2", "beta"])

    def test_underscore_separated(self):
        self.assertEqual(split("foo_bar_baz"), ["foo", "bar", "baz"])

    def test_mixed_separators(self):
        self.assertEqual(split("fooBar.bazQux"), ["foo", "bar", "baz", "qux"])

    def test_leading_and_trailing_separators(self):
        self.assertEqual(split("__helloWorld__"), ["hello", "world"])

    def test_only_separators(self):
        self.assertEqual(split("___"), [])

    def test_non_string_raises(self):
        with self.assertRaises(TypeError):
            split(123)

    def test_alias_matches_core(self):
        self.assertEqual(split("fooBar"), core_split("fooBar"))
        self.assertEqual(split_camel_case("fooBar"), split("fooBar"))


if __name__ == "__main__":
    unittest.main()
