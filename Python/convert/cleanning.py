import os, shutil
from tkinter import filedialog, messagebox
from pathlib import Path
from tkinter import*

#Designed to clean the selected directory.

def Clean(): 
  t= filedialog.askdirectory(title="clean the selected folder")
  dir = t
  for files in os.listdir(dir):
      path = os.path.join(dir, files)
      os.remove(path)
      messagebox.showinfo(":D it worked !")

def check():
  if not os.listdir('C:/Users/noeng/Documents/python/convert/downloads'):
      messagebox.showinfo("Folder Downloads is empty.", "Folder empty")
  else:
    for p in Path('C:/Users/noeng/Documents/python/convert/downloads').iterdir():
      messagebox.showinfo("in : C:/Users/noeng/Documents/python/convert/downloads", p)