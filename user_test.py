import unittest
from user import User
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        A method that runs before the test starts
        """
        self.new_user = User("Fitstar","Gillie2021")

    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.username,"Fitstar")
        self.assertEqual(self.new_user.password,"Gillie2021")

if __name__ == '__main__':
    unittest.main()

  
