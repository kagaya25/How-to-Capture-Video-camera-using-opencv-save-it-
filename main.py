import cv2
capture=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('Subscribe.mp4',fourcc,60.0,(640,480))
while(capture.isOpened()):
	ret,frame=capture.read()
	if(ret==True):
		out.write(frame)
		cv2.imshow('output',frame)
		if(cv2.waitKey(1) & 0xFF == ord('q')):
			break
	else:
		break	
capture.release()
cv2.destroyAllWindows()
