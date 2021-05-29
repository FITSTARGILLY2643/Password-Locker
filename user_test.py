import unittest
from user import User
from user import Credentials
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        A method that runs before the test starts
        """
        self.new_user = User("Fitstar","Gillie2021")

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_init(self):
        """
        test case to check if the object in initialized correctly
        """
        self.assertEqual(self.new_user.username,"Fitstar")
        self.assertEqual(self.new_user.password,"Gillie2021")
    
    def test_save_user(self):
        '''
        test case to check if the new instance of the user object has been created
        '''
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines the test cases for the class Credentials
    """
    def setUp(self):
        '''
         a method that runs before each individual credentials test methods run.
        '''
        self.new_credentials = Credentials("Gilbert","gillie2643","2643fits")

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []
    def test_details(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credentials.account,"Gilbert")
        self.assertEqual(self.new_credentials.username,"gillie2643")
        self.assertEqual(self.new_credentials.password,"2643fits")


if __name__ == '__main__':
    unittest.main()

  
