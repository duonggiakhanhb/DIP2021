# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer

from pathlib import Path
import cv2
import numpy as np
import imutils
import PIL
from PIL import Image, ImageTk
import pytesseract
import qr_extractor as reader
import pyzbar.pyzbar as pyzbar

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Canvas, NW, Label, Frame, END

width, height = 630, 430
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.bind('<Escape>', lambda e: destroyCap())

window.geometry("1074x682")
window.configure(bg="#FFFFFF")

canvas = Canvas(window,
                bg="#FFFFFF",
                height=682,
                width=1074,
                bd=0,
                highlightthickness=0,
                relief="ridge")

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
left_rtg = canvas.create_image(881.0, 379.0, image=image_image_1)

image_image_2 = PhotoImage(file=relative_to_assets("image_2.png"))
qr_rtg = canvas.create_image(881.0, 251.0, image=image_image_2)

image_image_3 = PhotoImage(file=relative_to_assets("image_3.png"))
qr_text = canvas.create_image(880.0, 127.0, image=image_image_3)

image_image_4 = PhotoImage(file=relative_to_assets("image_4.png"))
data_text = canvas.create_image(881.0, 378.0, image=image_image_4)

image_image_5 = PhotoImage(file=relative_to_assets("image_5.png"))
data_rtg = canvas.create_image(881.0, 476.0, image=image_image_5)

coppy_btn_image = PhotoImage(file=relative_to_assets("button_1.png"))
coppy_btn = Button(image=coppy_btn_image,
                   borderwidth=0,
                   bg="#FFFFFF",
                   highlightthickness=0,
                   command=lambda: print("button_1 clicked"),
                   relief="flat")
coppy_btn.place(x=756.0, y=579.0, width=107.0, height=42.0)

button_image_2 = PhotoImage(file=relative_to_assets("clear_btn.png"))
clear_btn = Button(image=button_image_2,
                   borderwidth=0,
                   bg="#FFFFFF",
                   highlightthickness=0,
                   command=lambda: clear(),
                   relief="flat")
clear_btn.place(x=898.0, y=579.0, width=107.0, height=42.0)

image_image_6 = PhotoImage(file=relative_to_assets("image_6.png"))
main_rtg = canvas.create_image(362.0, 308.0, image=image_image_6)

button_image_3 = PhotoImage(file=relative_to_assets("scan_btn.png"))
scan_btn = Button(image=button_image_3,
                  borderwidth=0,
                  bg="#FFFFFF",
                  highlightthickness=0,
                  command=lambda: [changeCap(), video_stream()],
                  relief="flat")
scan_btn.place(x=263.0, y=565.0, width=197.82608032226562, height=70.0)

image_image_7 = PhotoImage(file=relative_to_assets("image_7.png"))
logoApp = canvas.create_image(286.0, 48.0, image=image_image_7)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(image=button_image_4,
                  borderwidth=0,
                  bg="#FFFFFF",
                  highlightthickness=0,
                  command=lambda: print("button_4 clicked"),
                  relief="flat")
button_4.place(x=985.0, y=20.0, width=71.0, height=57.0)

entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(880.5, 475.5, image=entry_image_1)
entry_1 = Text(bd=0, bg="#FFFFFF", highlightthickness=0)
entry_1.place(x=748.0, y=415.0, width=265.0, height=119.0)

qrFrame = Canvas(window,
                 bg="#FFFFFF",
                 height=175,
                 width=175,
                 bd=0,
                 highlightthickness=0,
                 relief="ridge")
qrFrame.place(x=793, y=164)

# Function ----------------------------------------------------------------


def cutImage(im, new_width):
    height, width, chanels = im.shape  # Get dimensions
    left = int((width - new_width) / 2)
    # Crop the center of the image
    return im[:, left:left + new_width]


# Display ------------

app = Frame(window, bg="white")
app.place(x=47.5, y=93.5)
# Create a label in the frame
lmain = Label(app)
# lmain.place(x = 362.5, y = 308.5)
lmain.grid()


# Show qrcode detected in the frame
def showQr(img):

    #Resize the image
    image = cv2.resize(img, (175, 175))

    # Convert the image to a PhotoImage to display
    image = image.astype(np.uint8)
    im = Image.fromarray(image)
    image = ImageTk.PhotoImage(im)
    qrFrame.create_image(0.5, 0.5, anchor=NW, image=image)
    window.mainloop()


# Capture from camera
cap = cv2.VideoCapture(0)
capTurnOn = False


# function for video streaming
def video_stream():
    global capTurnOn
    if not capTurnOn:
        return
    _, frame = cap.read()
    frame = cv2.resize(frame, (frame.shape[1], height), cv2.INTER_AREA)
    frame = cutImage(frame, width - 2)
    data, warp, check = reader.extract(frame, True)
    if (check):
        data = data.decode("utf-8")
        entry_1.insert("1.0", data + "\n")
        showQr(warp)
        changeCap()
        return
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)


def clear():
    entry_1.delete("1.0", END)


def changeCap():
    global capTurnOn
    capTurnOn = not capTurnOn


def destroyCap():
    cap.release()
    cv2.destroyAllWindows()


window.resizable(False, False)
window.mainloop()