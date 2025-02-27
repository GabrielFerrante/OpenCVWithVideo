""" 
Como utilizar multiplos Streamings IP facilmente ? ImageZMQ

link: https://github.com/jeffbass/imagezmq

instalar: pip install imagezmq
"""

import cv2
import imagezmq
image_hub = imagezmq.ImageHub()
while True:
   rpi_name, image = image_hub.recv_image()
   cv2.imshow(rpi_name, image)
   cv2.waitKey(13)
   image_hub.send_reply(b'OK')