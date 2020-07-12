from serial import Serial
import time
import threading


class slaveController():
    def __init__(self):
        # Number of Locks:
        self.nLock = 4
        # Hex of sending unlocking signal to each lock:
        self.toUnlockHex = ['8a0101119b', '8a01021198', '8a01031199', '8a0104119e']
        # Hex of status read from each lock:
        # Locked succeed:
        self.lockSucceedHex = ['8101010081', '8101020082', '8101030083', '8101040084']
        # Unlock succeed:
        self.unlockSucceedHex = ['8101011190', '8101021193', '8101031192', '8101041195']
        # Unlock failed:
        self.unlockFailedHex = ['810101008a', '8a01020089', '8a01030088', '8a0104008f']
        try:
            self.port = Serial("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", 9600)
        except:
            print ("Cannot establish Serial connection to specified port")

    def __del__(self):
        # if self.port.is_open():
        #     self.port.close()
        pass
    def send_to_port(self, lockNum):
        '''
            it will take a lockNum and unlock the corresponding locker to that
            lock number in success it will return True else its a False
        '''
        try:
            self.port.open()
        except:
            print ("Cannot open serial port")
            return False

        if lockNum<0 or lockNum > 4:
            print("Invalid input, please try again.")
            self.port.close()
            return False
        else:
            self.port.flushOutput()
            self.port.write(bytes.fromhex(toUnlockHex[lockNum-1]))
        self.port.close()
        return True
        # while True:
        #     time.sleep(1)
        #     # lockNum = int(input("to lock #: "))
        #     #print(lockNum, type(lockNum))
        #     if lockNum<0 or lockNum > 4:
        #         print("Invalid input, please try again.")
        #         break
        #     else:
        #         print("Unlocking lock ", lockNum)
        #         port.write(bytes.fromhex(toUnlockHex[lockNum-1]))

    def read_from_port(self):
        try:
            self.port.open()
        except:
            print ("Cannot open serial port")
            return

        port.flushInput()
        reading = read(port.inWaiting())
        #
        # Some logic code based on readings to determine the state of the lock
        #
        self.port.close()
        return lock or unlocked
        # while True:
        #     time.sleep(0.3)
        #     b = port.read(port.inWaiting())
        #     for i in range(nLock):
        #         if self.lockSucceedHex[i] in b.hex():
        #             print("Lock ", i+1, " locked successfully")
        #         if self.unlockSucceedHex[i] in b.hex():
        #             print("Lock ", i+1, " unlocked successfully")
        #         if self.unlockFailedHex[i] in b.hex():
        #             print("Lock ", i+1, " unlocked failed")
        #         if self.toUnlockHex[i] in b.hex():
        #             print("Lock ", i+1, "is unlocked already")
    def wait_till_locker_closes(self, locker_num):
        '''
            this function will run in an infinite loop until the locker_num is closed
        '''
        pass


# try:
#     port =slaveController()
#     thread = threading.Thread(target= port.read_from_port))
#     thread.start()
#     send_to_port()
# except KeyboardInterrupt:
#     thread.join()


#at this point the door must be open.
# executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
# check_res = executor.submit(self.check_pass, passcode)
