import cv2

import qr_extractor as reader
import matplotlib.pyplot as plt

# cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
img = cv2.imread("qr1.jpg")
codes, frame = reader.extract(img, True)
cv2.imshow("frame", frame)

# When everything done, release the capture
# cap.release()
# frame = cv2.imread("qr.jpg")
# plt.imshow(frame)
# plt.show()
# codes, frame = reader.extract(frame, True)
# cv2.imshow("frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
