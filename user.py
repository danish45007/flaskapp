class User:

    def __int__(self,username,email,password):
        self.username = username
        self.email  = email
        self.password = password

     @staticmethod
    def is_authenticated(self):
        return True
    @staticmethod
    def is_active(self):
        return True
    @staticmethod
    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username
