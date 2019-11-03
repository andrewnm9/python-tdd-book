from django.test import TestCase


class TestBasic(TestCase):

    def test_bad_maths(self):
        self.assertEqual(1, 3 + 2)
