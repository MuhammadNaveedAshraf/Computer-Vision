# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:34:39 2021

@author: emnas
"""
#https://machinelearningmastery.com/how-to-perform-face-detection-with-classical-and-deep-learning-methods-in-python-with-keras/
from cv2 import imread
from cv2 import CascadeClassifier
import cv2
import mtcnn
import tensorflow as tf
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from mtcnn.mtcnn import MTCNN


def face_detection_with_openCV(image):
    # load the photograph
    pixels = imread(image)
    # load the pre-trained model
    classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
    # perform face detection
    bboxes = classifier.detectMultiScale(pixels,1.01,8)
    # print bounding box for each detected face
    for box in bboxes:
	    print(box)
    for (x,y,w,h) in bboxes:
        cv2.rectangle(pixels, (x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("faces",pixels)
    cv2.waitKey(0)
#face_detection_with_openCV('faces4.jpg')

 
# draw an image with detected objects
def draw_image_with_boxes(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
	# plot the image
	pyplot.imshow(data)
	# get the context for drawing boxes
	ax = pyplot.gca()
	# plot each box
	for result in result_list:
		# get coordinates
		x, y, width, height = result['box']
		# create the shape
		rect = Rectangle((x, y), width, height, fill=False, color='red')
		# draw the box
		ax.add_patch(rect)
	# show the plot
	pyplot.show()

def get_drawn_image(filename,faces):
    data=cv2.imread(filename)
    #pyplot.imshow(data)
    #ax=pyplot.gca()
    for face in faces:
        x,y,width,height=face['box']
        cv2.rectangle(data, (x,y),(x+width,y+height),(0,255,0),2)
        
        #ax.add_patch(rect)
    return data

# draw each face separately
def draw_faces(filename, result_list):
	# load the image
	data = pyplot.imread(filename)
	# plot each face as a subplot
	for i in range(len(result_list)):
		# get coordinates
		x1, y1, width, height = result_list[i]['box']
		x2, y2 = x1 + width, y1 + height
		# define subplot
		pyplot.subplot(1, len(result_list), i+1)
		pyplot.axis('off')
		# plot face
		pyplot.imshow(data[y1:y2, x1:x2])        
	# show the plot
	pyplot.show()

def get_faces_from_image(imagename,faces):
    data=cv2.imread(imagename)
    facesgot=[]
    for i in range(len(faces)):
        x1,y1,width,height=faces[i]['box']
        x2,y2=x1+width, y1+height
        facesgot.append(data[y1:y2, x1:x2])
    return facesgot
filename = 'faces2.jpg'
# load image from file
pixels = pyplot.imread(filename)
# create the detector, using default weights
detector = MTCNN()
# detect faces in the image
faces = detector.detect_faces(pixels)
# display faces on the original image
data=get_drawn_image(filename,faces)
cv2.imshow("faces",data)
cv2.waitKey(0)
facesgot=get_faces_from_image(filename, faces)
draw_faces(filename, faces)
