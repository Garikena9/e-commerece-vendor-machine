class Vendor:

    def login(self, username, password):
        """This method will be used to login an existing Vendor."""
        pass
class GuidoVanRossum(Vendor):
    def login(self, username, password):
        username = "Rossum"
        password = "rossum_pw"
        pass
class JamesGosling(Vendor):

    def logout(self):
        """This method will be used to logout an existing Vendor."""
        pass