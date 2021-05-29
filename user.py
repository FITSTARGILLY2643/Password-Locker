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