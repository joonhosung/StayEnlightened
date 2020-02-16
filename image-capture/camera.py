import cv2

def capture():
	# this function receives no parameters
	# returns cv2 im file (so the one we passed into imsave)
	webcam = cv2.VideoCapture(0);
	check, frame = webcam.read();
	cv2.imshow("Capturing", frame); #grab, decode and return next frame from video
	cv2.imwrite(filename='saved_img.jpg', img = frame) #Optionally save file as .jpg
	webcam.release()
	cv2.destroyAllWindows()
	return frame
