from Camera import Camera
import time

camera = Camera(0, 'saved_img.jpg') #no self 

for x in range(0, 3):
	frame = camera.capture()
	print("Took a picture.")
	time.sleep(3) #Wait 7 secs to take another picture