import cv2
import tkinter as tk
from PIL import Image, ImageTk, ImageFont,ImageDraw
from pocketsphinx import LiveSpeech
import threading

root = tk.Tk()
root.title("Real-Time Sinhala Subtitle Generator")

canvas = tk.Canvas(root, width=640, height=480)
canvas.pack()


root.mainloop()