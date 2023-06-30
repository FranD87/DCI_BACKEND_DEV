from django.test import TestCase, tag
from .forms import BlogForm, form_is_good
from .utils import add_items
import logging
#  python manage.py test --verbosity 2 checks all info of the test
# Create your tests here.

class AddFunctionTestCase(TestCase):
    """ Test for blog app"""

    def test_add_function(self):
        expected_result = 30
        result = add_items(10,20)
        self.assertIsNotNone(result)


# class BlogTestCase(TestCase):
    # '''Test for Blog app'''
    # def setUp(self):
    #     print("setting up before each test method")
    #
    # @classmethod
    # def setUpClass(cls):
    #     print("setting up before running all tests ....")
    #
    # def tearDown(self) -> None:
    #     print("tearing down after each test method")
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print("tear down after all tests ....")
    #
    # @tag('blogvalues', 'blg_val')
    # def test_equal_values(self):
    #     value_1: int = 123
    #     value_2: int = 123
    #     value_3: int = '123'
    #     self.assertEqual(value_1, value_2)
    # def test_equal_values_failed(self):
    #     value_1: int = 123
    #     value_2: int = 123
    #     value_3: int = '123'
    #     self.assertEqual(value_1, value_2)
    #
    # def test_form_is_valid(self):
    #     '''Test to check data that makes the form Valid'''
    #     form_data = {
    #         "title": "Test Title",
    #         "name": "Test Name",
    #         "email": "test@sample.com"
    #     }
    #     blog_form = BlogForm(form_data)
    #     self.assertTrue(blog_form.is_valid())
    #
    # def test_form_is_not_valid(self):
    #     '''Testing if Blog form is not valid'''
    #     form_data = {
    #         #"title": "Test Title",
    #         "name": "Test Name",
    #         "email": "test@sample.com"
    #     }
    #     blog_form = BlogForm(form_data)
    #     self.assertFalse(blog_form.is_valid())
    #
    # # def test_assert_is_none(self):
    # #     var = form_is_good(BlogForm)
    # #     self.assertIsNone(var)
    #
    # def test_home_page(self):
    #     url: str = "/"
    #     expected_status_code: int = 200
    #     un_expected_status_code: int = 404
    #     unexpected_codes: int = [201, 202, 301, 302, 400, 404]
    #     response = self.client.get(url)
    #     content = response.content.decode("utf-8")
    #     print("status_code:", response.status_code)
    #     print("content:", content)
    #     self.assertEqual(response.status_code, expected_status_code)
    #     self.assertNotEqual(response.status_code, un_expected_status_code)
    #     self.assertIn("blog", content)
    #     self.assertNotIn(response.status_code, unexpected_codes)
    #
    # def test_redirect_page(self):
    #     url: str = "/redirect/"
    #     expected_status_code: int = 302
    #     response = self.client.get(url)
    #     print("status_code:", response.status_code)
    #     self.assertEqual(response.status_code, expected_status_code)
    #
    # def test_create_page(self):
    #     url: str = "/create_page/"
    #     post_data: str = {
    #         "name": "Danielle",
    #         "age": 300,
    #     }
    #     expected_status_code: int = 200
    #     response = self.client.post(url, data=post_data)
    #     content = response.content.decode("utf-8")
    #     response_info = response.wsgi_request
    #     data_sent = response_info.body.decode("utf-8")
    #     print(content)
    #     print(data_sent)
    #     self.assertEqual(response.status_code, expected_status_code)
    #     self.assertIn("create", content)
    #     self.assertIn("age", data_sent)
