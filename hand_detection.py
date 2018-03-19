
import cv2
#from Image import *
from webcam import WebcamVideoStream
from detections import Detection


class HandTracker:

    def __init__(self):
        self.webcam = WebcamVideoStream()
        self.webcam.start()
        self.detection = Detection()
        
        #hand gesture status
        self.is_okay = False
        self.is_vhand = False
        self.is_phand = False
        
        #get location of hand when tracking
        self.x_axis = 0.0
        self.y_axis = 0.0


    def _start_up(self):
        
        while  self.is_okay == False:
        # get image from webcam
            image = self.webcam.read()

        # look for the OK sign to start up
            self.is_okay = self.detection.is_item_detected_in_image('data/ok_cascade_48x48.xml', image )
            
            if self.is_okay:
             # recognized OK Sign
                print("OK GESTURE Detected ")
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
            self.is_vhand = self.detection.is_item_detected_in_image('data/vhand_cascade.xml', image )
            self.is_phand =self.detection.is_item_detected_in_image('data/phand_cascade.xml', image )
        #check which hand gesture detected

            if self.is_vhand:
             # v-sign
                print("V-SIGN detected (Turn on/off Lights)")
                self.x_axis= self.detection.x_axis
                self.y_axis=self.detection.y_axis
                print("x_axis: " , self.x_axis , "y_axis: " , self.y_axis)
            if self.is_phand:
                print("P-SIGN detected (Lamp follows hand gesture) ")
            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break
        return
            
    def _powerButton(self):
        #turn on/off L.E.D
        
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
