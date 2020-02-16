import cv2

def capture():
	# this function receives no parameters
	# returns cv2 im file (so the one we passed into imsave)
	webcam = cv2.VideoCapture(0);
	check, frame = webcam.read();
	cv2.imshow("Capturing", frame);
	cv2.imwrite(filename='saved_img.jpg', img = frame)
	webcam.release()
	cv2.destroyAllWindows()
	return img
