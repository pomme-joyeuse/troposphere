import os
import tkinter as tk
from tkinter import messagebox
from pytubefix import YouTube
from pathlib import Path

def video():
    url = e1.get().strip()
    yt = YouTube(url)

       # Progressive = video + audio together
    stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    destination = Path('C:/Users/noeng/Documents/Python/convert/downloads') 

        # Download
    stream.download(output_path=destination)
    messagebox.showinfo("Success", f"Downloaded: {yt.title}")