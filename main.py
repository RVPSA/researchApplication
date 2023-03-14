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

# Sample text
#from this list we show word in the opencv frame
text = ["",""]

# variable for trained speech recognition file
hmm = 'C:\\Users\\mrsak\\OneDrive\\Desktop\\New folder (6)\\test1000\\test1000.ci_cont'
lm = 'C:\\Users\\mrsak\\OneDrive\\Desktop\\New folder (6)\\test1000\\test1000.lm.bin'
dict = 'C:\\Users\\mrsak\\OneDrive\\Desktop\\New folder (6)\\test1000\\test1000.dic'
wrds = []

#function that recognize speeches
def speech():
    recognizer = LiveSpeech(verbose=False, sampling_rate=16000, buffer_size=2048,
                            no_search=False, full_utt=False, hmm=hmm, lm=lm, dict=dict)

    for phrase in recognizer:
        mystring = phrase.hypothesis()
        print(mystring)
        print(type(mystring))
        wrds.append(mystring)
        fhandle = open("transcribe.txt", "w", encoding='utf-8')
        fhandle.writelines(" %s " % wrd for wrd in wrds)
        text.append(mystring)
        print('wrote to the file')
        fhandle.close()
t1 = threading.Thread(target=speech)


#function that enables opencv camera
def show_frame():
    _, frame = cap.read()  # read a frame from the camera
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # convert the color from BGR to RGB

    img = Image.fromarray(frame)  # create a PIL Image from the frame

    # Draw non-ascii text onto image
    font = ImageFont.truetype("C:\Windows\Fonts\\Nirmala.ttf", 20)
    draw = ImageDraw.Draw(img)
    draw.text((30, 400), text[-2]+" "+text[-1], font=font)

    img_tk = ImageTk.PhotoImage(image=img)  # convert the PIL Image to a Tkinter-compatible image
    canvas.img_tk = img_tk  # keep a reference to the image to prevent garbage collection
    canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)  # display the image on the canvas
    root.after(10, show_frame)  # schedule the next call to show_frame after 10 milliseconds


show_frame()
t1.start()
root.mainloop()