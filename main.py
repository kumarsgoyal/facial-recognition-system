from tkinter import *
import os
from datetime import datetime

# creating instance of TK
root = Tk()

root.configure(background="white")


# root.geometry("300x300")
def function1():
	os.system("python add_user.py")


def function2():
    os.system("python train_classifier.py")


def function3():
    os.system("python face_recognition.py")
    os.system("afplay sound.mp3")


def function6():
    root.destroy()


#def attend():
#	path = ((os.getcwd()) + "/firebase/attendance_files/attendance" + str(datetime.now().date()) + ".xls")
#	os.popen(path,'r',100)
    #os.popen(os.getcwd() + "/firebase/attendance_files/attendance" + str(datetime.now().date()) + ".xls",'r',1000)


# stting title for the window
#root.title("AUTOMATIC ATTENDANCE MANAGEMENT USING FACE RECOGNITION")
root.title("ATTENDANCE MANAGEMENT")
# creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 20), fg="yellow", bg="Green", height=4).grid(row=0, rowspan=2, columnspan=2, sticky=N + E + W + S, padx=10, pady=10)

# creating first button
Button(root, text='Add User', font=("times new roman", 30), bg="white", fg='Red', command=function1).grid(row=3, columnspan=2, sticky=W + E + N + S, padx=5, pady=5)

# creating second button
Button(root, text="Train Dataset", font=("times new roman", 30), bg="white", fg='Red', command=function2).grid(row=4, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating third button
Button(root, text="Attendance", font=('times new roman', 30), bg="white", fg="Red", command=function3).grid(row=5, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)

# creating attendance button
#Button(root, text="Attendance Sheet", font=('times new roman', 20), bg="white", fg="maroon", activeforeground="maroon", command=attend).grid(row=6, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)


Button(root, text="Exit", font=('times new roman', 30), bg="white", fg="Red", command=function6).grid(row=9, columnspan=2, sticky=N + E + W + S, padx=5, pady=5)


root.mainloop()
