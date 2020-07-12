import serial
import time
import threading

# Number of Locks:
nLock = 4
# Hex of sending unlocking signal to each lock:
toUnlockHex = ['8a0101119b', '8a01021198', '8a01031199', '8a0104119e']
# Hex of status read from each lock:
# Locked succeed:
lockSucceedHex = ['8101010081', '8101020082', '8101030083', '8101040084']

# Unlock succeed:
unlockSucceedHex = ['8101011190', '8101021193', '8101031192', '8101041195']

# Unlock failed:
unlockFailedHex = ['810101008a', '8a01020089', '8a01030088', '8a0104008f']

ser = serial.Serial("/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0", 9600)
ser.flushInput()
#ser.flushOutput()

def send_to_port():
    while True:
        time.sleep(1)
        lockNum = int(input("to lock #: "))
        #print(lockNum, type(lockNum))
        if lockNum!=1 and lockNum!=2 and lockNum!=3 and lockNum!=4:
            print("Invalid input, please try again.")
            continue
        else:
            print("Unlocking lock ", lockNum)
            ser.write(bytes.fromhex(toUnlockHex[lockNum-1]))

def read_from_port(ser):
    while True:
        time.sleep(0.3)
        b = ser.read(ser.inWaiting())

        for i in range(nLock):

            if lockSucceedHex[i] in b.hex():

                print("Lock ", i+1, " locked successfully")
                
            if unlockSucceedHex[i] in b.hex():
                print("Lock ", i+1, " unlocked successfully")
                
            if unlockFailedHex[i] in b.hex():
                print("Lock ", i+1, " unlocked failed")
                
            if toUnlockHex[i] in b.hex():
                print("Lock ", i+1, "is unlocked already")
                
try:
    thread = threading.Thread(target=read_from_port, args=(ser,))
    thread.start()
    send_to_port()
except KeyboardInterrupt:
    thread.join()
    ser.close()
