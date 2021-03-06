import unittest

from ponthe import app

class ProjectTests(unittest.TestCase):
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.app.get('/v1/')
        self.assertEqual(302, response.status_code)


if __name__ == "__main__":
    unittest.main()
