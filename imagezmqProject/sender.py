import cv2
import imagezmq
import time
import imutils

sender = imagezmq.ImageSender()
image_window_name = 'camera_1'
previous = time.time()
delta = 0
vs = cv2.VideoCapture('http://honjin1.miemasu.net/nphMotionJpeg?Resolution=640x480&Quality=Standard')

while True:
   ret,frame = vs.read()
   current = time.time()
   delta += current - previous
   previous = current
   if delta > 3 :
      grabbed, frame = vs.read()
      frame = imutils.resize(frame,500)
      delta = 0
      text1 = sender.send_image(image_window_name, frame)