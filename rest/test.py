from models import Application
from database import db_session
import unittest


class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.app = Application('myproject')

    def test_name(self):
        self.assertEqual(self.app.name, 'myproject', msg='Project name may exists.')

    def test_serial(self):
        self.assertNotEqual(self.app.serial, '', msg="Serial is null! It shouldnt be null.")

    def test_id_is_null(self):
        self.assertEqual(self.id, None, msg='When instantiating a new object Your ID should be None.')

    def test_saving(self):
        print db_session.add(self.app)
        db_session.commit()

if __name__ == '__main__':
    unittest.main()