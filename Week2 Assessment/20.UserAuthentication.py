from abc import ABC, abstractmethod
class UserAuthentication(ABC):
    @abstractmethod
    def login(self):
        pass
    @abstractmethod
    def logout(self):
        pass
class GoogleAuth(UserAuthentication):
    def login(self):
        print('Google login')

    def logout(self):
        print('Google logout')
class FacebookAuth(UserAuthentication):
    def login(self):
        print('Facebook login')

    def logout(self):
        print('Facebook logout')
def main():
    g = GoogleAuth()
    g.login()
    g.logout()
    f = FacebookAuth()
    f.login()
    f.logout()
main()