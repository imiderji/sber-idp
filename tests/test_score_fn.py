from score_functions import score_fn
import unittest


class TestScoreFn(unittest.TestCase):

    """ Класс с unit-тестами для функции score_fn"""

    def test_perfect_match(self):
        """
        Тест на полное совпадение.
        """

        gold = 'PER_Maxim, ORG_SBER'
        pred = 'PER_Maxim, ORG_SBER'
        f1, precision, recall = score_fn(gold, pred)

        self.assertEqual(f1, 1.0)
        self.assertEqual(precision, 1.0)
        self.assertEqual(recall, 1.0)

    def test_half_match(self):
        """
        Тест на совпадение половины сущностей.
        """

        gold = 'PER_Maxim, ORG_SBER'
        pred = 'PER_Maxim, ORG_Avito'
        f1, precision, recall = score_fn(gold, pred)

        self.assertEqual(f1, 0.5)
        self.assertEqual(precision, 0.5)
        self.assertEqual(recall, 0.5)

    def test_partial_match(self):
        """
        Тест на частичное совпадение сущностей.
        """

        gold = 'PER_Maxim, ORG_SBER, LOC_Moscow'
        pred = 'PER_Maxim, ORG_Avito, LOC_Moscow'
        f1, precision, recall = score_fn(gold, pred)

        self.assertAlmostEqual(f1, 0.667, delta=0.001)
        self.assertAlmostEqual(precision, 0.667, delta=0.001)
        self.assertAlmostEqual(recall, 0.667, delta=0.001)

    def test_pr_disbalance(self):
        """
        Тест, при котором Precision > Recall.
        """

        gold = 'PER_Maxim, ORG_SBER, LOC_Moscow'
        pred = 'PER_Maxim'
        f1, precision, recall = score_fn(gold, pred)

        self.assertAlmostEqual(precision, 1.0, delta=0.001)
        self.assertAlmostEqual(recall, 0.333, delta=0.001)
        self.assertFalse(precision == recall)
        self.assertAlmostEqual(f1, 0.5, delta=0.001)

    def test_no_match(self):
        """
        Тест на нулевое совпадение.
        """

        gold = 'PER_Maxim, ORG_SBER'
        pred = 'PER_Andrew, ORG_Avito'
        f1, precision, recall = score_fn(gold, pred)

        self.assertEqual(f1, 0.0)
        self.assertEqual(precision, 0.0)
        self.assertEqual(recall, 0.0)

    def test_no_gold_entities(self):
        """
        Тест-кейс LLM перепредсказала сущности.
        """

        gold = ''
        pred = 'LOC_Moscow, PRO_Neuroslav'
        f1, precision, recall = score_fn(gold, pred)

        self.assertEqual(f1, 0.0)
        self.assertEqual(precision, 0.0)
        self.assertEqual(recall, 0.0)

    def test_no_pred_entities(self):
        """
        Тест-кейс LLM не выделила сущности.
        """

        gold = 'LOC_Moscow, PRO_GigaChat'
        pred = ''
        f1, precision, recall = score_fn(gold, pred)

        self.assertEqual(f1, 0.0)
        self.assertEqual(precision, 0.0)
        self.assertEqual(recall, 0.0)

    def test_empty_pred_and_gold(self):
        """
        Тест-кейс с пустой разметкой.
        """

        gold = ''
        pred = ''
        f1, precision, recall = score_fn(gold, pred)

        self.assertEqual(f1, 0.0)
        self.assertEqual(precision, 0.0)
        self.assertEqual(recall, 0.0)
