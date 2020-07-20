from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2

from DPLSystem.DB.dbHandler import dbHandler

class Scanner():
    def __init__(self):
        self.vs = VideoStream(usePiCamera=True).start()
        time.sleep(0.5)

    def __del__(self):
        cv2.destroyAllWindows()

    def resultInDB(self, barcodeData):
        '''
        To check if the scanned barcode content matches the tracking number in database
        return true if so, otherwise return false.
        '''
        dbContent = dbHandler()
        if dbContent.get_delivery_by_trackingNumber(barcodeData) is not None:
            return True
        else:
            return False

    def getScannedResult(self):
        '''
        main scanner function, scan barcode and qrcode, get content of the barcode and qrcode.
        barcodeData: variable with a value of the content scanned from barcode or qrcode.
        '''
        while True:
            frame = self.vs.read()
            frame = imutils.resize(frame, width=400)
            barcodes = pyzbar.decode(frame)
            for barcode in barcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                barcodeData = barcode.data.decode("utf-8")
                barcodeType = barcode.type
                text = "{} ({})".format(barcodeData, barcodeType)
                cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                print("scanned result: ", barcodeData)
                if self.resultInDB(barcodeData):
                    print("in database")
                    break # can change this line to return the scanned result for further reference.
                else:
                    print("scanned barcode data is not in dababase")
                    continue


            cv2.imshow("Barcode Scanner", frame)
            key = cv2.waitKey(1) & 0xFF



# uncomment codes below to test this file
scan = Scanner()
scan.getScannedResult()


