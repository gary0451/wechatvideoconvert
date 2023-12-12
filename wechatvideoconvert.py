import tkinter as tk
from tkinter import ttk
import tkinterDnD  # Importing the tkinterDnD module
import ffmpeg
import os

filepath = ''
filefolder = ''
filename = ''
tempfile = ''

def drop(event):
    filepath = event.data
    filefolder = getfilefolder(filepath)
    filename = getfilename(filepath)
    convideo(filepath)
    delfile(filepath)
    stringvar.set("完成！")

def delfile(filename):
    os.remove(filename)
    oldfile = filepath
    newfile = filefolder + filename
    tempfile = filefolder + "temp.mp4"
    os.rename(tempfile, newfile)

def convideo(fileName):
    stream = ffmpeg.input(fileName)
    stream = ffmpeg.output(stream,"temp.mp4")
    ffmpeg.run(stream,overwrite_output=True)

def getfilefolder(filepath):
    filepathlist = filepath.split('/')
    filename = filepathlist[-1]
    filefolder = filepath.rstrip(filename)
    return filefolder

def getfilename(filepath):
    filepathlist = filepath.split('/')
    filename = filepathlist[-1]
    return filename

root = tkinterDnD.Tk()  
root.title("微信视频转换")
root.geometry("300x300")
stringvar = tk.StringVar()
stringvar.set('Drag and drop here!')


label_1 = tk.Label(root, textvar=stringvar, relief="solid")
label_1.pack(fill="both", expand=True, padx=10, pady=10)

label_1.register_drop_target("*")
label_1.bind("<<Drop>>", drop)



root.mainloop()

