from django.test import TestCase
from .models import Link
import uuid
import datetime


class ModelChangedTestCase(TestCase):
    def setUp(self) -> None:
        link = Link.objects.create(initial_link='http://google.com')

    def test_field_difference(self):
        link = Link.objects.first()

        initial_link_url = link.initial_link
        link.initial_link = 'http://amazon.com'
        link.save()
        new_link_url = link.initial_link

        self.assertNotEqual(initial_link_url, new_link_url)

    def test_model_change(self):
        link = Link.objects.first()
        is_changed_start = link.has_changed
        link.initial_link = 'http://amazon.com'
        link.save()
        is_changed_end = link.has_changed

        self.assertNotEquals(is_changed_start, is_changed_end)

    def test_difference(self):
        link = Link.objects.first()
        link.initial_link = 'http://amazon.com'
        link.save()

        self.assertIsNotNone(link.get_field_diff('initial_link'))

    def test_changed_fields(self):
        link = Link.objects.first()
        link.initial_link = 'http://amazon.com'
        link.created = datetime.datetime.now()
        link.save()

        self.assertEqual(len(link.changed_fields), 1)


class LinkSerializerTestCase(TestCase):

    def setUp(self) -> None:
        link = Link.objects.create(initial_link='http://google.com')
