from unittest import TestCase

from project import main, settings
from project.utils import get_environ_json


class TestUtils(TestCase):

    def test_get_environ_json(self):
        json = get_environ_json()
        self.assertIn('"DUMMY": {}'.format(str(settings.DUMMY).lower()), json)
        self.assertIn('"USER": "{}"'.format(settings.USER), json)
