
import cv2
#from Image import *
from webcam import WebcamVideoStream
from detections import Detection

is_okay = False

class HandTracker:

    def __init__(self):
        self.webcam = WebcamVideoStream()
        self.webcam.start()
        self.detection = Detection()

        self.x_axis = 0.0
        self.y_axis = 0.0


    def _start_up(self):
        global is_okay

        while is_okay == False:
        # get image from webcam
            image = self.webcam.read()

        # look for the OK sign to start up
            is_okay = self.detection.is_item_detected_in_image('data/ok_cascade_48x30.xml', image )

            if is_okay:
             # recognized OK Sign
                print("OK SIGN ")
            # move to modes stage
                self._modes()

            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break


    def _modes (self):
        while True:
        # get image from webcam
            image = self.webcam.read()

        #different classifier for different modes
            is_vicky = self.detection.is_item_detected_in_image('data/face.xml', image )

        #check which hand gesture detected

            if is_vicky:
             # v-sign
                print("FACE ")
            if cv2.waitKey(1) == 27 :
                self.webcam.stop()
                self.webcam.stream.release()
                break
        return

    #stops webcam and return camera
    def _shut_down (self):
        self.webcam.stop()
        self.webcam.stream.release()

    def main(self):
        # setup and run OpenGL
        return

# run instance of Hand Tracker
handTracker = HandTracker()
handTracker._start_up()

cv2.destroyAllWindows()
