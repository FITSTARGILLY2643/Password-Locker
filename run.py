from user import User,Credentials
def create_new_user(username,password):
    """
    function that creates a user using a password and username
    """
    new_user = User(username,password) 
    return new_user

def save_user(user):
    """
    function that saves a new user
    """
    user.save_user()