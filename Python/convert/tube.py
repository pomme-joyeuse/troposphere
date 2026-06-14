from pytubefix import YouTube 
from tkinter import*
import moviepy.editor
from tkinter import messagebox
from pathlib import Path
# Convert a YouTube url into a video.


def video():
	url = str(input("entrez un url : \n>> "))
	video = YouTube(url, 'WEB')
	tt = video.title
	stream = video.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
	# check for destination to save file 
	destination = Path('C:/Users/noeng/Documents/Python/convert/downloads') 
	t = stream.download(output_path=destination)
	video = moviepy.editor.VideoFileClip(t) 
	messagebox.showinfo("Video sucessfully downloaded", tt)