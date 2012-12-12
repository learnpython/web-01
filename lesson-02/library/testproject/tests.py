from unittest import TestCase

from library import to_json


class TestLibrary(TestCase):

    def test_to_json(self):
        data = [1, 2, 3, 4]
        dumped = to_json(data)
        self.assertEqual(dumped.count('    '), 4)

        data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
        dumped = to_json(data)
        self.assertEqual(dumped.count('    '), 4)
