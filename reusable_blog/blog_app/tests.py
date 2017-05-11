# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from .models import Post

# Create your tests here.
class PostTests(TestCase):
    """
    Here we will define the tests
    that we will run againts our Post model
    """
    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                         'My Latest Bloggy Post')