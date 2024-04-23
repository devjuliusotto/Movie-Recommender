import unittest
from app import create_app, db
from app.models import Movie

class BasicTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_movie(self):
        response = self.client.post('/', data=dict(title="Test Movie", genre="Test Genre"), follow_redirects=True)
        self.assertIn(b"Test Movie", response.data)

if __name__ == '__main__':
    unittest.main()
