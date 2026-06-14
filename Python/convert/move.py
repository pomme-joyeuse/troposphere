import shutil
import os
from tkinter import filedialog
from tkinter import messagebox

#code to change the location on the selected file

def move():
	old = filedialog.askopenfilename(title="Select input", filetypes=())
	destination = filedialog.askdirectory(title="Select directory")
	shutil.move(old, destination)	
	messagebox.showinfo("files moved to : ",destination)