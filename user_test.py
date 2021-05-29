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

    def test_save_credentials(self):
        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credentials.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_many_account(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_user_credentials()
        test_credential = Credentials("Marrie","Marrien","marrie340")
        test_credential.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

     
    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials('Marrie','Marrien','Marrien340')
        test_credentials.save_user_credentials()

        the_credential = Credentials.find_by_number("Marrie")
        self.assertEqual(the_credential.account,test_credentials.account)

    def test_creditial_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials('Marrie','Marrien','Marrien340')
        test_credentials.save_user_credentials()
        
        found_credential = Credentials.credentials_exist("Marrie")
        self.assertTrue(found_credential)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials('Marrie','Marrien','Marrien340')
        test_credentials.save_user_credentials()
        
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()

  
