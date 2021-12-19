import cv2

import qr_extractor as reader
import matplotlib.pyplot as plt
from PIL import Image

# cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
#     codes, frame = reader.extract(frame, True)
#     cv2.imshow("frame", frame)
    
#     # codes = zbarlight.scan_codes(['qrcode'], codes)
#     # print('QR codes: %s' % codes)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         print("I quit!")
#         break

# When everything done, release the capture
# cap.release()
frame = cv2.imread("./../qr1.jpg")

codes, frame, check = reader.extract(frame, True)

cv2.imshow("frame", frame)
cv2.waitKey(0)
plt.imshow(frame)
plt.show()
cv2.destroyAllWindows()
