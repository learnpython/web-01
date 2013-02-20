from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.db import DatabaseError
from django.test import TestCase

from .models import Bookmark


TEST_EMAIL = 'user@zozozo.com'
TEST_PASSWORD = 'password'
TEST_USERNAME = 'user'

TEST_TITLE = 'Google'
TEST_URL = 'http://www.google.com/'
TEST_DESCRIPTION = 'Test Description'


class TestModels(TestCase):

    def setUp(self):
        kwargs = {
            'username': TEST_USERNAME,
            'password': TEST_PASSWORD,
            'email': TEST_EMAIL,
        }
        self.user = User.objects.create_user(**kwargs)

    def test_create_update(self):
        kwargs = {
            'user': self.user,
            'title': TEST_TITLE,
            'url': TEST_URL,
        }
        bookmark = Bookmark.objects.create(**kwargs)
        self.assertEqual(len(bookmark.uid), 4)

        kwargs['title'] = kwargs['title'][::-1]
        self.assertRaises(ValidationError, Bookmark.objects.create, **kwargs)

        old_uid = bookmark.uid
        bookmark.title = TEST_TITLE[::-1]
        bookmark.save()

        self.assertEqual(bookmark.uid, old_uid)

    def test_create_update_big_description(self):
        kwargs = {
            'user': self.user,
            'title': TEST_TITLE,
            'url': TEST_URL,
            'description': ' ' * 1001,
        }
        self.assertRaises(ValidationError, Bookmark.objects.create, **kwargs)

        kwargs['description'] = TEST_DESCRIPTION
        bookmark = Bookmark.objects.create(**kwargs)

        bookmark.description = ' ' * 1001
        self.assertRaises(ValidationError, bookmark.save)


class TestViews(TestCase):

    def setUp(self):
        self.old_USE_I18N = settings.USE_I18N
        settings.USE_I18N = False

        self.index_url = reverse('index')

    def tearDown(self):
        settings.USE_I18N = self.old_USE_I18N

    def test_index(self):
        pass

    def test_index_empty(self):
        response = self.client.get(self.index_url)
        self.assertContains(response, '<h3>Warning</h3>')
        self.assertContains(response, '<p>No bookmarks found in database.</p>')
