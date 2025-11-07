import tkinter as tk
from tkinter import *
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.font as font
import pyttsx3

# project module
import show_attendance
import takeImage
import trainImage
import automaticAttedance

def text_to_speech(user_text):
    engine = pyttsx3.init()
    engine.say(user_text)
    engine.runAndWait()

haarcasecade_path = "haarcascade_frontalface_default.xml"
trainimagelabel_path = "./TrainingImageLabel/Trainner.yml"
trainimage_path = "/TrainingImage"
if not os.path.exists(trainimage_path):
    os.makedirs(trainimage_path)

studentdetail_path = "./StudentDetails/studentdetails.csv"
attendance_path = "Attendance"

window = Tk()
window.title("Face Recognizer")
window.geometry("1280x720")
window.configure(background="#ffffff")  # White modern theme

# ---------------- Header ----------------
header_frame = Frame(window, bg="#4da6ff", height=70)
header_frame.pack(fill=X)

header_label = Label(
    header_frame,
    text="CLASS VISION",
    bg="#4da6ff",
    fg="white",
    font=("Helvetica", 26, "bold")
)
header_label.pack(pady=10)

# ---------------- Logo ----------------
logo = Image.open("UI_Image/0001.png")
logo = logo.resize((50, 47), Image.LANCZOS)
logo1 = ImageTk.PhotoImage(logo)
logo_label = tk.Label(window, image=logo1, bg="#ffffff")
logo_label.place(x=460, y=80)

# ---------------- Title ----------------
title_label = tk.Label(
    window,
    text="Welcome to CLASS VISION",
    bg="#ffffff",
    fg="#333333",
    font=("Helvetica", 32, "bold")
)
title_label.pack(pady=30)

# ---------------- Button style helpers ----------------
def on_enter(e):
    e.widget["background"] = "#1a75ff"

def on_leave(e):
    e.widget["background"] = "#4da6ff"

def create_button(text, command, x, y):
    btn = tk.Button(
        window,
        text=text,
        command=command,
        bd=0,
        bg="#4da6ff",
        fg="white",
        font=("Helvetica", 15, "bold"),
        height=2,
        width=20,
        relief="flat",
        cursor="hand2",
        activebackground="#1a75ff",
        activeforeground="white"
    )
    btn.place(x=x, y=y)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn

# ---------------- Image icons ----------------
ri = Image.open("UI_Image/register.png")
r = ImageTk.PhotoImage(ri)
label1 = Label(window, image=r, bg="#ffffff")
label1.place(x=100, y=270)

ai = Image.open("UI_Image/attendance.png")
a = ImageTk.PhotoImage(ai)
label2 = Label(window, image=a, bg="#ffffff")
label2.place(x=980, y=270)

vi = Image.open("UI_Image/verifyy.png")
v = ImageTk.PhotoImage(vi)
label3 = Label(window, image=v, bg="#ffffff")
label3.place(x=600, y=270)

# ---------------- Sub-window (Register UI) ----------------
def TakeImageUI():
    ImageUI = Tk()
    ImageUI.title("Register Student")
    ImageUI.geometry("780x480")
    ImageUI.configure(background="#ffffff")
    ImageUI.resizable(0, 0)

    Label(ImageUI, text="Register Your Face", bg="#4da6ff", fg="white",
          font=("Helvetica", 26, "bold"), height=2).pack(fill=X)

    Label(ImageUI, text="Enter the details", bg="#ffffff", fg="#333333",
          font=("Helvetica", 20, "bold")).place(x=280, y=90)

    lbl1 = Label(ImageUI, text="Enrollment No", bg="#ffffff", fg="#333333",
                 font=("Helvetica", 14, "bold"))
    lbl1.place(x=120, y=160)
    txt1 = Entry(ImageUI, width=20, bd=2, bg="#f0f0f0", fg="#000000",
                 font=("Helvetica", 14))
    txt1.place(x=300, y=160)

    lbl2 = Label(ImageUI, text="Name", bg="#ffffff", fg="#333333",
                 font=("Helvetica", 14, "bold"))
    lbl2.place(x=120, y=210)
    txt2 = Entry(ImageUI, width=20, bd=2, bg="#f0f0f0", fg="#000000",
                 font=("Helvetica", 14))
    txt2.place(x=300, y=210)

    message = Label(ImageUI, text="", width=30, bg="#ffffff", fg="#1a75ff",
                    font=("Helvetica", 12, "bold"))
    message.place(x=220, y=260)

    def take_image():
        try:
            l1 = txt1.get()
            l2 = txt2.get()
            takeImage.TakeImage(l1, l2, haarcasecade_path, trainimage_path, message,
                            None, text_to_speech)
            txt1.delete(0, "end")
            txt2.delete(0, "end")
        except tk.TclError:
            print("Window closed before completion.")
        

    def train_image():
        try:
            trainImage.TrainImage(haarcasecade_path, trainimage_path,
                              trainimagelabel_path, message, text_to_speech)
        except tk.TclError:
            print("Window closed before completion.")
        

    btn_take = create_button("Take Image", take_image, 150, 330)
    btn_train = create_button("Train Image", train_image, 400, 330)

# ---------------- Main Buttons ----------------
create_button("Register a New Student", TakeImageUI, 100, 520)

def automatic_attedance():
    automaticAttedance.subjectChoose(text_to_speech)

create_button("Take Attendance", automatic_attedance, 600, 520)

def view_attendance():
    show_attendance.subjectchoose(text_to_speech)

create_button("View Attendance", view_attendance, 1000, 520)

create_button("EXIT", window.destroy, 600, 660)

# ---------------- Footer ----------------
Label(window, text="Developed by Team | Face Recognition Attendance",
      bg="#ffffff", fg="#777777", font=("Helvetica", 10)).pack(side="bottom", pady=10)

window.mainloop()
