import cv2
import tkinter as tk
from PIL import Image, ImageTk, ImageFont,ImageDraw
from pocketsphinx import LiveSpeech
import threading

root = tk.Tk()
root.title("Real-Time Sinhala Subtitle Generator")

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()

cap = cv2.VideoCapture(0)  # use the default camera (index 0)

#function that enables opencv camera
def show_frame():
    _, frame = cap.read()  # read a frame from the camera
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert the color from BGR to RGB

    img = Image.fromarray(frame)  # create a PIL Image from the frame

    img_tk = ImageTk.PhotoImage(image=img)  # convert the PIL Image to a Tkinter-compatible image
    canvas.img_tk = img_tk  # keep a reference to the image to prevent garbage collection
    canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)  # display the image on the canvas
    root.after(10, show_frame)  # schedule the next call to show_frame after 10 milliseconds


show_frame()
root.mainloop()