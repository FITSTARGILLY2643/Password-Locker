import random
import string
class User:
    """
    Class that generates instance of a user,list of users and their passwords
    """
    user_list=[]
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user is a method that saves the user to the user_list
        """
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def display_user(cls):
        """
        a method that display a list of users
        """
        return cls.user_list

class Credentials:
     """
        a class that generates an istance of an account credentials and a list of credentials

     """
     credentials_list = []
     def __init__(self,account,username,password):
         self.account = account
         self.username = username
         self.password = password

     @classmethod
     def verify_user(cls,username,password):
        a_user = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                a_user == user.username
                return a_user

     def save_user_credentials(self):
        """
        save_user_credential method saves a new user object to credentials list
        """
        Credentials.credentials_list.append(self)

     def delete_credentials(self):
        """
        delete saved credentials in the credentials list
        """
        Credentials.credentials_list.remove(self)


       
