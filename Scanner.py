from imutils.video import VideoStream
from pyzbar import pyzbar
import imutils
import time
import cv2
# from DPLSystem.DB.dbHandler import dbHandler

class Scanner():
    def __init__(self):
        self.vs = VideoStream(usePiCamera=True).start()
#         self.vs = VideoStream(src=0).start()
        self.result = False
#         time.sleep(2.0)

    def __del__(self):
        cv2.destroyAllWindows()

    def resultInDB(self, barcodeData):
        '''
        To check if the scanned barcode content matches the tracking number in database
        return: true if so, otherwise return false.
        '''
#         dbContent = dbHandler()
#         below is the final version code, uncomment below for final version
#         if dbContent.get_delivery_by_trackingNumber(barcodeData) is not None:
#             return True
#         else:
#             return False

#         below is the test version of code, test with get_delivery_by_trackingNumber_test function in dbHandler. Remove these for final version.
#         if dbContent.get_delivery_by_trackingNumber_test(barcodeData) == barcodeData:
#             return True
#         else:
#             return False
#         
        return True

    def getScannedResult(self):
        print("getScannedResult")
        '''
        main scanner function, scan barcode, get tracking number of barcode
        barcodeData: scanned tracking number
        return: True if tracking number is in database; False is tracking number is not in database after scanned for 3 times.
        
        '''
        
        counter = 0
        maxScanningTime = 3 # this will allow user to scan for up to 3 times.
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
                    print("in database ", barcodeData)
                    self.result = True
                    cv2.destroyAllWindows()
                    self.vs.stop()
                    return True # tracking number is not in database
                else:
                    print("tracking number ", barcodeData, "is not in database")
                    time.sleep(3)
                    counter += 1
                    if counter < maxScanningTime:
                        continue # keep scanning until meet max scanning time
                    else:
                        self.result = False
                        cv2.destroyAllWindows()
                        self.vs.stop()
                        return False # return false if tracking number is not in database after scanning for 3 times.

            cv2.imshow("Barcode Scanner", frame)
            key = cv2.waitKey(1) & 0xFF



# uncomment codes below to test this file
scan = Scanner()
A = scan.getScannedResult()
print(A)
