import cv2

class Detection(object):
    def __init__(self):
        self.x_axis = 0.0
        self.y_axis = 0.0
        
    def is_item_detected_in_image(self, item_cascade_path, image):
        # detect items in image
        item_cascade = cv2.CascadeClassifier(item_cascade_path)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        items = item_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=4 )

        # debug: draw rectangle around detected items
        for (x,y,w,h) in items:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
            #print ("*****new x ", x , "****new y" , y )
            self.x_axis= x
            self.y_axis= y
        # debug: show detected items in window
        cv2.imshow('OpenCV Detection', image)

        # indicate whether item detected in image
        return len(items) > 0
