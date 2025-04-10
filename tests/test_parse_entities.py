from score_functions import parse_entities
import unittest


class TestParseEntities(unittest.TestCase):

    """ Класс с unit-тестами для функции parse_entities. """

    def test_empty_string(self):
        """
        Тест с пустой строкой.
        """
        self.assertEqual(parse_entities(''), set())

    def test_no_entities(self):
        """
        Тест со строкой из пробелов.
        """
        self.assertEqual(parse_entities('     '), set())

    def test_single_entity(self):
        """
        Тест с одной сущностью.
        """
        self.assertEqual(parse_entities('PER_Maxim'), {('PER', 'Maxim')})

    def test_multiple_entities(self):
        """
        Тест с несколькими сущностями.
        """
        entities = 'PER_Maxim, ORG_SBER'
        exceptation = {('PER', 'Maxim'), ('ORG', 'SBER')}

        self.assertEqual(parse_entities(entities), exceptation)

    def test_duplicate_entities(self):
        """
        Тест с дубликатами.
        """
        entities = 'LOC_Moscow, LOC_Moscow'
        exceptation = {('LOC', 'Moscow')}

        self.assertEqual(parse_entities(entities), exceptation)

    def test_multiword_entities(self):
        """
        Тест с сущностью из нескольких слов.
        """
        entities = 'LOC_Смоленская область'
        exceptation = {('LOC', 'Смоленская область')}

        self.assertEqual(parse_entities(entities), exceptation)

    def test_entities_with_underlines(self):
        """
        Тест с разделителем "_" внутри сущности.
        """
        entities = 'PRO_snake_case'
        exceptation = {('PRO', 'snake_case')}

        self.assertEqual(parse_entities(entities), exceptation)
