from app import api

# Importamos a biblioteca de testes
import unittest


class TestHomeView(unittest.TestCase):
    def setUp(self):
        app = api.test_client()
        self.response = app.get('/')

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_html_string_response(self):
        self.assertEqual("WORKING", self.response.data.decode('utf-8'))

    def test_html_string_worng_response(self):
        self.assertNotEqual("WORKING1", self.response.data.decode('utf-8'))

    def test_content_type(self):
        self.assertIn('text/html', self.response.content_type)
