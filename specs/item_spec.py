import unittest
from app import create_app
from db.db import db


class ItemTestCase(unittest.TestCase):
    """This class represents the bucketlist test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app('development')
        self.client = self.app.test_client

        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.session.close()
            db.drop_all()
            db.create_all()


    def test_item_creation(self):

        res = self.client().post(
            '/api/item/abdo',
   
            data={'price': 12.12})
        self.assertEqual(res.status_code, 201)
        # print(res.data)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
