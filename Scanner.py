from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2
import operator

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
    help="path to output CSV file containing barcodes")
args = vars(ap.parse_args())
found = dict()
csv = open(args["output"], "w")
print("[INFO] starting video stream...")
# vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)


def fromScanner(found, vs):
# loop over the frames from the video stream

    #print(found.items())
    # grab the frame from the threaded video stream and resize it to
    # have a maximum width of 400 pixels
    frame = vs.read()
    frame = imutils.resize(frame, width=400)

    # find the barcodes in the frame and decode each of the barcodes
    barcodes = pyzbar.decode(frame)

    # loop over the detected barcodes
    for barcode in barcodes:
        # extract the bounding box location of the barcode and draw
        # the bounding box surrounding the barcode on the image
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # the barcode data is a bytes object so if we want to draw it
        # on our output image we need to convert it to a string first
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(frame, text, (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        # if the barcode text is currently not in our CSV file, write
        # the timestamp + barcode to disk and update the set
        if barcodeData not in found:
            found[barcodeData] = 1
        
        if barcodeData in found:
            found[barcodeData] += 1
            
    # show the output frame
    cv2.imshow("Barcode Scanner", frame)
    key = cv2.waitKey(1) & 0xFF
    
def endPoint(content, phone):
    csv.write("{},{},{}\n".format(datetime.datetime.now(), content, phone))
    csv.flush()
    csv.close()
    cv2.destroyAllWindows()     

def startPoint():
    found = dict()
    # initialize the video stream and allow the camera sensor to warm up
    print("To end the program safely with an output of the detected content from the scanner, simply press 'q' on keyboard. ")
    # open the output CSV file for writing and initialize the set of
    # barcodes found thus far

    
    while True:
        try:
            fromScanner(found, vs)
        except KeyboardInterrupt:
            break 

    # close the output CSV file do a bit of cleanup
    print("[INFO] cleaning up...")
    content = max(found.items(), key=operator.itemgetter(1))[0]
    print("Final detected content is: ")
    print(content)
    contentCorrect = input("Is this content correct? [y/n] ")
    while contentCorrect != 'y' and contentCorrect != 'n' and contentCorrect != 'Y' and contentCorrect != 'N':
        print("invalid input, please try again!")
        contentCorrect = input("Is this content correct? [y/n] ")
    if contentCorrect == 'n' or contentCorrect == 'N':
        enterContent = input("choose the method you would like to enter code contents: 1. scan again 2. user input from keyboard [1/2] ")
        while enterContent != '1' and enterContent != '2':
            print("invalide input, please try again!")
            enterContent = input("choose the method you would like to enter code contents: 1. scan again 2. user input from keyboard [1/2] ")
        if enterContent == '1':
            startPoint()
        if enterContent == '2':
            content = input("Please enter the correct content: ")
            phone = input("Please enter the package receiver's phone number: ")
            endPoint(content, phone)
    if contentCorrect == 'y' or contentCorrect == 'Y':
        phone = input("Please enter the package receiver's phone number: ")
        endPoint(content, phone)

startPoint()


