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

def display_user(user):
    """
    function that displays user
    """
    return User.display_user()

def login_user(password,username):
    """
    a function that checks if the users already exist 
    """
    checked_user = Credentials.verify_user(password,username)
    return checked_user

def create_new_credential(account,username,password):
    """
    function that create new credential details for a new user
    """
    new_credential = Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    """
    a function that addes a new credential to the credential
    """
    credentials.save_user_credentials()

def delete_credentials(credentials):
    """
    a function that deletes credentials from the credential list
    """
    credentials.delete_credentials()

def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_by_number(account)

def check_credentials(account):
    """
    a function that checks if the credentials of the searched name exist and return true or false
    """
    return Credentials.credentials_exist(account)

def generate_password(self):
    """
    a function that generates password randomly
    """
    auto_password = Credentials.generate_password(self)
    return auto_password