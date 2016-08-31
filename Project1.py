#Digital Multimedia - Assignment 1
#Author: Dustin Grady
#Purpose: To create a filter by finding the median of each pixel, and outputting the result
#Status: In progress/ Untested

from __future__ import print_function
from PIL import Image
import statistics

imageContainer = []#List to contain our images
pixelContainer = []#List to contain our pixel values
finalImageElements = []#List to hold pixels that will compose our final image

for i in range(1, 10):#Get each image and add it to our list
    img = Image.open('C:/Users/Gish-Laptop/CS205_Project1/Project 1 Images/' + str(i) +'.png')#Open image
    imageContainer.append(img)#Add image to list

def processImage(img):
    xSize, ySize = img.size#Get dimensions of current image
    px = img.load()#Will hold individual pixel value
    
    for y in range (0, ySize):
        for x in range (0, xSize):
            pixelContainer.append(px[x,y])
    getMedian(pixelContainer)#Get the median of the current pixel
            
def getMedian(pixelContainer):
    medianPixel = statistics.median(pixelContainer)
    finalImageElements.append(medianPixel)
        
processImage(img)#Call our function to run

#finalImage = Image.new(img.mode, img.size)
#finalImage.putdata(pixelContainer)
#finalImage.show()


