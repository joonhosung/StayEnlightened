import cv2

# Class for all camera functions
class Camera():
	
	def __init__(self, index, file):
		#self.webcam = cv2.VideoCapture(index)
		#self.file = file

	def capture(self):
		# this function receives no parameters
		# returns cv2 im file (so the one we passed into imsave)
		self.webcam = cv2.VideoCapture(index)
		self.file = file
		if not self.webcam.isOpened():
			raise Exception("Could not open video device")

		check, frame = self.webcam.read()
		
		if check:
			cv2.imshow("Capturing", frame); #grab, decode and return next frame from video
			cv2.imwrite(filename=self.file, img = frame) #Optionally save file as .jpg
		self.webcam.release()
		cv2.destroyAllWindows()
		return frame
