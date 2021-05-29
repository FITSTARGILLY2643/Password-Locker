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