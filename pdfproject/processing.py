import extract
import skew
import getlines
import cv2
import json


def process(pdf, coarse_rotate_angle):
	""" Extract images, fix skew, and get line positions, writing images and data to files. There is no return value."""

	## Get images from PDF
	images = extract.extractImages(pdf)
	## Straighten images
	if coarse_rotate_angle < 0:
		coarse_rotate_angle = 360 - (abs(coarse_rotate_angle) % 360)
	else:
		coarse_rotate_angle = coarse_rotate_angle % 360
	print "angle:" + str(coarse_rotate_angle)
	images = [skew.straighten(skew.coarserotate(i, coarse_rotate_angle)) for i in images]
	print "images found: " + str(len(images))

	## Iterate through list of images, storing lists of corresponding line locations
	## in hash table.
	## Then write each image to file.
	## File naming convention: <original filename><page number>.jpg
	n=1
	lines = {} 
	for i in images:
		p = pdf+str(n)+".jpg"
		lines[n]=getlines.getLines(i)
		cv2.imwrite(p,i)
		n = n+1
	## Write line data in JSON format to a .txt file
	## File naming convention: <original filename>.json.txt
	with open ((pdf+".json.txt"),'w') as outfile:
		json.dump(lines,outfile)
