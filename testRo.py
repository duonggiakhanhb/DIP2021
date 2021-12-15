import cv2
import math
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('test.jpg')
img = cv2.resize(img, (0, 0), fx=2, fy=2)
rows,cols,ch = img.shape

cv2.imshow('image',img)
cv2.waitKey(0)

pts1 = np.float32([[127,148],[323,62],[545, 289],[406,437]])

ratio=0.75
cardH=math.sqrt((pts1[2][0]-pts1[1][0])*(pts1[2][0]-pts1[1][0])+(pts1[2][1]-pts1[1][1])*(pts1[2][1]-pts1[1][1]))
cardW=ratio*cardH
pts2 = np.float32([[pts1[0][0],pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]], [pts1[0][0]+cardW, pts1[0][1]+cardH], [pts1[0][0], pts1[0][1]+cardH]])

M = cv2.getPerspectiveTransform(pts1,pts2)

offsetSize=500
transformed = np.zeros((int(cardW+offsetSize), int(cardH+offsetSize)), dtype=np.uint8);
dst = cv2.warpPerspective(img, M, transformed.shape)
print()
for x in range (0,4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])), 5, (0,0,255), -1)
plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()