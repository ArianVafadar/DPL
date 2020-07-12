from .DB.dbHandler import dbHandler
from .HAL.slaveController import slaveController

class UIHandler():
    def __init__(self):
        self.db = dbHandler()
        self.slaveCntr = slaveController()
    def __del__(self):
        pass
    def verifyPasscode(self, passcode_list):
        '''
            checks the user passcode to make sure it matches a delivery, if it does
            it'll return True else return False
            - verify passcode with DB
            - unlock the locker (idk how to check if its locked)
            - change the state of t
        '''
        passcode = "".join([el for el in passcode_list])
        if not self.db.get_delivery_by_passcode(passcode):
            return False
        locker_num = int(passcode[2:4])
        if not self.slaveCntr.send_to_port(locker_num): #unlock the locker
            print("something went wrong with the slave controller")
            return False
        return True

    def wait_till_locker_closes(self,passcode):
        '''
            stall till the locker is closed and upon closing it will update the
            status of delivery
        '''
        locker_num = int(passcode[2:4])
        self.slaveCntr.wait_till_locker_closes(locker_num)
        #@todo: once wait_till_locker_closes is finished
        #the strucutre should be like this: while(unlocked): sleep(1); keep checking;

        delivery=self.db.get_delivery_by_passcode(passcode)
        self.db.update_delivery_status(delivery.delivery_id, "picked-up")

        self.db.update_locker_state(locker_num,"available")
        #push to servers?

    def verifyCameraRecordings(self, locker_num):
        pass
