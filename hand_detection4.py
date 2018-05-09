
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
        self.is_okay  = False
        self.is_vhand = False
        self.is_phand = False
        self.is_palm  = False
        self.is_fist  = False

        #get location of hand when tracking
        self.x_axis = 0.0
        self.y_axis = 0.0

        #get tracker location
        self.yprime_axis = 0
        self.xprime_axis = 0

        #get middle of frame
        self.x_center = (self.webcam.camera().get(cv2.CAP_PROP_FRAME_WIDTH))/2;
        self.y_center = (self.webcam.camera().get(cv2.CAP_PROP_FRAME_HEIGHT))/2;


    def _start_up(self):

        while  self.is_okay == False:
        # get image from webcam
            image = self.webcam.read()
            print("WAITING FOR OK SIGN")

        # look for the OK sign to start up
            self.is_okay = self.detection.is_item_detected_in_image('data/ok_cascade_48x30.xml', image )

            if self.is_okay:
             # recognized OK Sign
                print("OK GESTURE Detected ")
                self.is_okay = False
            # move to modes stage
                self._modes()

            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break


    def _modes (self):
        # Look to recognize a gesture
        while True:
        # get image from webcam
            image = self.webcam.read()

        #different classifier for different modes
            #self.is_phand = self.detection.is_item_detected_in_image('data/face.xml', image )
            self.is_fist =self.detection.is_item_detected_in_image('data/fist.xml', image )
            #self.is_vhand =self.detection.is_item_detected_in_image('data/.xml', image )
            #self.is_palm =self.detection.is_item_detected_in_image('data/palm.xml', image )

        #check which hand gesture detected

            #Fist hand gesture
            if self.is_fist:
               self.is_fist = False
               print("Fist detected, See if it moved" )
               self.x_axis= self.detection.x_axis
               self.y_axis=self.detection.y_axis
               self._keepCenter(self.x_axis,self.y_axis)

            #Phand gesture
            if self.is_phand:
               self.is_phand = False
               print("Phand detected, See if it moved" )
               self.x_axis= self.detection.x_axis
               self._moveFocus(self.x_axis)
            #Vhand gesture
            if self.is_vhand:
               self.is_vhand = False
               print("Vhand detected, See if it moved" )
               self.x_axis= self.detection.x_axis
               self._changeLight(self.x_axis)
            #Palm gesture
            if self.is_palm:
               self.is_palm = False
               print("Palm detected, See if it moved" )
               self.x_axis= self.detection.x_axis
               self._powerLight(self)
            #Escape from program
            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break
        return

    def _powerButton(self):
        #turn on/off L.E.D

        return

    def _keepCenter(self , x_axis ,y_axis):
        flag = True
        x = 25
        while x != 0:
        # get image from webcam
            image = self.webcam.read()

        #different classifier for different modes
            self.is_fist = self.detection.is_item_detected_in_image('data/face.xml', image )

        #check which hand gesture detected

            if self.is_fist:
                x = 25
                self.is_fist = False
                #Get new position x and y positions
                self.xprime_axis= self.detection.x_axis
                self.yprime_axis=self.detection.y_axis

                #If the new position is different from the intial position take the absoute value to find the difference
                if ((self.xprime_axis != self.x_axis  or  self.yprime_axis != self.y_axis) and (flag == True)):
                            dx = self.xprime_axis - self.x_axis
                            dx = abs(dx)

                            dy = self.yprime_axis - self.y_axis
                            dy = abs(dy)

                            print("x_axis: " , self.x_axis , " y_axis: " , self.y_axis)
                            print("Face MOVED xprime_axis: " , self.xprime_axis , "FACE moved yprime_axis: " , self.yprime_axis)
                            print("dx: ", dx , "dy: ", dy)

                            #if above threshold for movement
                            if( dx >= 20 or dy >= 20 ):

                                #Hand Ready to be Tracked
                                flag = False
                #If the new position is not equal to the center of the screen continue
                if ((self.xprime_axis != self.x_center  or  self.yprime_axis != self.y_center) and (flag == False)):

                            print("Face centering Going on")

                            # Calculate how far away from the center
                            dx = self.xprime_axis - self.x_center
                            dx = abs(dx)

                            dy = self.yprime_axis - self.y_center
                            dy = abs(dy)

                            print("Face MOVED CENTERX_axis: " , self.x_center , "FACE moved CENTERY_axis: " , self.y_center)
                            print("Face MOVED xprime_axis: " , self.xprime_axis , "FACE moved yprime_axis: " , self.yprime_axis)
                            #if above threshold for movement
                            if( dx >= 20 or dy >= 20 ):
                                print("Movement of Motors")
                                self._moveMotors(self.xprime_axis,self.yprime_axis,dx,dy)

            else:
                print("No Gesture Detected")
                x = x-1


            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break

        print("___________****TIME OUT*****__________")
        self._start_up()
        return

    def _moveFocus(self , x_axis):
        flag = True
        x = 25
        while x != 0:
        # get image from webcam
            image = self.webcam.read()

        #different classifier for different modes
            self.is_phand = self.detection.is_item_detected_in_image('data/fist.xml', image )

        #check which hand gesture detected

            if self.is_phand:
                x = 25
                self.is_phand = False
                #Get the new x position
                self.xprime_axis= self.detection.x_axis
                #If the new x position is different from the intial position take the absoute value to find the difference
                if ((self.xprime_axis != self.x_axis) and (flag == True)):
                            dx = self.xprime_axis - self.x_axis
                            dx = abs(dx)

                            print("x_axis: " , self.x_axis)
                            print("Phand MOVED xprime_axis: " , self.xprime_axis)
                            print("dx: ", dx)

                            #if above threshold for movement
                            if( dx >= 20):

                                #Hand Ready to be Tracked
                                flag = False

                #If the new position is not equal to the center of the screen continue
                if ((self.xprime_axis != self.x_center) and (flag == False)):

                            print("Phand centering Going on")

                            # Calculate how far away from the center
                            dx = self.xprime_axis - self.x_center
                            dx = abs(dx)

                            print("Phand MOVED CENTERX_axis: " , self.x_center)
                            print("Phand MOVED xprime_axis: " , self.xprime_axis)
                            #if above threshold for movement
                            if( dx >= 20):
                                print("Adjust Focus")
                                self._moveMotors(self.xprime_axis,-1,dx,-1)

            else:
                print("No Gesture Detected")
                x = x-1


            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break

        print("___________****TIME OUT*****__________")
        self._start_up()
        return

    def _changeLight(self , x_axis):
        x = 25
        while x != 0:
        # get image from webcam
            image = self.webcam.read()

        #different classifier for different modes
            self.is_vhand = self.detection.is_item_detected_in_image('data/fist.xml', image )

        #check which hand gesture detected

            if self.is_vhand:
                x = 25
                self.is_vhand = False
                #Get new x position
                self.xprime_axis= self.detection.x_axis
                #If the new position is different from the intial position take the absoute value to find the difference
                if ((self.xprime_axis != self.x_axis) and (flag == True)):
                            dx = self.xprime_axis - self.x_axis
                            dx = abs(dx)

                            print("x_axis: " , self.x_axis)
                            print("Vhand MOVED xprime_axis: " , self.xprime_axis)
                            print("dx: ", dx)

                            #if above threshold for movement
                            if( dx >= 20):

                                #Hand Ready to be Tracked
                                flag = False

                #If the new position is not equal to the center of the screen continue
                if ((self.xprime_axis != self.x_center) and (flag == False)):

                            print("Vhand centering Going on")

                            #Calculate how far away from the center
                            dx = self.xprime_axis - self.x_center
                            dx = abs(dx)

                            print("Vhand MOVED CENTERX_axis: " , self.x_center)
                            print("Vhand MOVED xprime_axis: " , self.xprime_axis)
                            #if above threshold for movement
                            if( dx >= 20):
                                print("Adjust Light Intensity")
                                self._moveMotors(self.xprime_axis,-1,dx,-1)

            else:
                print("No Gesture Detected")
                x = x-1


            if cv2.waitKey(1) == 27 :
                self._shut_down()
                break

        print("___________****TIME OUT*****__________")
        self._start_up()
        return

    def _powerLight(self):
        print(" LIGHTS ON/OFF " )

        return

    def _moveMotors(xpos,ypos, dx, dy):
        xcounter = 0
        ycounter = 0
        #If the new position is to the left of the center
        if(xpos < x_center):
            #Increase the motor
            print("")
            if( xcounter < dx):
                #MOTOR INCREASE FUNCTION
                print("")
                increase()
                xcounter = xcounter+1

        #If the new position is to the right of the center
        elif( xpos > x_center):
            #Decrease the motor
            print("")
            if( xcounter < dx):
                #MOTOR DECREASE FUNCTION
                print("")
                decrease()
                xcounter = xcounter+1

        #If the new position is above the center
        if((ypos < y_center) and (ypos != -1)):
            #Increase the MOTOR
            if( ycounter < dy):
                print("")
                #MOTOR INCREASE FUNCTION
                increase()
                ycounter = ycounter+1

        #If the new position is below the centering
        elif((ypos > y_center) and (ypos != -1)):
            print("")
            #Decrease the Motor
            if( ycounter < dy):
                #MOTOR DECREASE FUNCTION
                print("")
                decrease()
                ycounter = ycounter+1


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
