
import cv2
  
from matplotlib import pyplot as plt
  
img = cv2.imread(‘aksPedar’,0)
  
# find frequency of pixels
histr = cv2.calcHist([img],[0],None,[256],[0,256])
  
# showing the plot
plt.plot(histr)
plt.show() 
