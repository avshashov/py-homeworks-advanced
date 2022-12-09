from unittest import TestCase
from hw_collections import visits_from_russia, get_unique_ids, get_dict


class TestMain(TestCase):
    def test_visits(self):
        logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        self.assertEqual(visits_from_russia(), logs)

    def test_unique_ids(self):
        ids = [98, 35, 15, 213, 54, 119]
        self.assertEqual(get_unique_ids(), ids)

    def test_dict(self):
        self.assertIsInstance(get_dict(), dict)