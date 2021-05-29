import unittest
from user import User
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        A method that runs before the test starts
        """
        self.new_user = User("Fitstar","Gillie2021")

  
