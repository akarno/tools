# https://docs.python.org/3/library/unittest.mock.html
# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python
# http://fgimian.github.io/blog/2014/04/10/using-the-python-mock-library-to-fake-regular-functions-during-tests/
# https://www.blog.pythonlibrary.org/2016/07/19/python-201-an-intro-to-mock/
# https://blog.fugue.co/2016-02-11-python-mocking-101.html

from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock
#from blog import Blogsx as Blog
from blog import Blogsx
import requests

class TestBlog(TestCase):
    @patch('blog.Blogsx')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
            }
        ]

        response = blog.posts('test_uri')
        #print(response)
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

class TestBlog2(TestCase):
    @patch('blog.Blogsx.req_get')
    def test_blog_postsx(self, MockReq):
        blog = Blogsx('aaa')

        blog.req_get = MockReq('uri')
        #print(type(blog.req_get))
        blog.req_get.return_value = [
            {
                'userId': 1,
                'id': 1,
                'title': 'Test Title',
            }
        ]

        response = blog.posts('test_uri')
        #print(response)
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)


class TestBlog3(TestCase):
    @patch('blog.Blogsx.req_get')
    def test_blog_postsx(self, MockReq):
        blog = Blogsx('aaa')

        blog.req_get = MockReq('uri')
        blog.req_get.side_effect = [
            requests.ConnectionError('Test error'),
            MagicMock(status_code=200, headers={'content-type': "application/json"},
                      text='response_text')
        ]
        #print(type(blog.req_get))

        response = blog.posts('test_uri')
        #print(response)
        self.assertIsNotNone(response)
        #self.assertIsInstance(response, str)


class TestBlog4(TestCase):
    @patch('blog.Blogsx.req_get')
    def test_blog_postsx(self, MockReq):
        blog = Blogsx('aaa')

        blog.req_get = MockReq('uri')
        blog.req_get.side_effect = MagicMock(status_code=200, text='response_text')

        print(type(blog.req_get))

        response = blog.posts('test_uri')
        print(response.text)
        self.assertIsNotNone(response)
        #assert response.text == 'response_text'
        #self.assertIsInstance(response, str)