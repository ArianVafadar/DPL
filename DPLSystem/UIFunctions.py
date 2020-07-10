from .DB.dbHandler import dbHandler

class UIHandler():
    def __init__(self):
        self.db = dbHandler()
    def __del__(self):
        pass
    def verifyPasscode(self, passcode_list):
        # passcode is a list of character encoded integers
        passcode = "".join([el for el in passcode_list])
        #dummy operations to check compatibility
        temp = int(passcode_list[-1])
        if self.db.testFunc(temp) == -1:
            return False
        return True

    def verifyCameraRecordings(self):
        pass
    def test(self, x):
        return False
