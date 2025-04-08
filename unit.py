import unittest
import requests
class TestPageAccessibility(unittest.TestCase):

    def test_page_accessibility(self):
        url = 'https://kivy.org/doc/stable/gettingstarted/intro.html'
        response = requests.get(url)
        self.assertEqual(response.status_code, 200, f"Page {url} is not accessible. Status code: {response.status_code}")

if __name__ == '__main__':
    unittest.main()