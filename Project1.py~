#Project 1
#Author: Dustin Grady
#Github: https://github.com/G-I-S-H/CS205_Project1
#Purpose: To create a filter which will remove undesirable pixels by finding the median value through multiple images
#Status: Finished/ Tested

from PIL import Image
import statistics

imageContainer = []
pixels = []
finalImageElements = []#List to hold pixels that will compose our final image
inputValue = int(input('Enter # of photos: '))

#Get each image and add it to our list
for i in range(1, (inputValue + 1)):
    img = Image.open('C:/Users/Gish-Laptop/Documents/CS205_Project1/Project 1 Images/' + str(i) +'.png')
    imageContainer.append(img)

#Create a 2D list of lists array to hold pixel values
for i in range(0, inputValue):
    pixels.append([])

def processImage(img, inputValue):
    xSize, ySize = img.size#Get dimensions of current image

    #Put all pixels values into our 2D list of lists
    for z in range (0, inputValue):#Loops as many times as there are images
        for x in range (0, xSize):#Get pixels on x axis
            for y in range (0, ySize):#Get pixels on y axis
                r, g, b = imageContainer[z].getpixel((x,y))#Break pixel into its R,G,B elements
                pixels[z].append((r,g,b))#Append those values as tuple to pixels container

    #Get pixel values from images (same pixel coordinates) find median, and send to final image
    for i in range (len(pixels[0])):#Each image should have the same amount of pixels, reference first
        tempPixels = []
        for x in range(inputValue):#Go through each image
            tempPixels.append(pixels[x][i])#Append corresponding pixels to a temp list to be processed
        finalImageElements.append(statistics.median_high(tempPixels))#Find the median, add to another list (median_high allows even numbers of images to be used)

    finalImage = Image.new('RGB', img.size)
    img = finalImage.load()

    #Assemble final image
    count = 0
    for x in range (0, xSize):
        for y in range (0, ySize):
            img[x,y] = finalImageElements[count]
            count += 1
    finalImage.show()#Show the result    

processImage(img, inputValue)#Run the algorithm
