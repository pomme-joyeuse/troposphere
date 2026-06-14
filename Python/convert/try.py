import os
import tkinter as tk
from tkinter import filedialog, messagebox
from pytubefix import YouTube

def video():
    try:
        url = entry.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL.")
            return

        yt = YouTube(url)

        # Progressive = video + audio together
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()

        if not stream:
            messagebox.showerror("Error", "No progressive streams found!")
            return

        destination = Path('C:/Users/noeng/Documents/Python/convert/downloads') 

        # Download
        stream.download(output_path=destination)
        messagebox.showinfo("Success", f"Downloaded: {yt.title}")

    except Exception as e:
        messagebox.showerror("Download Failed", str(e))


# Tkinter GUI
root = tk.Tk()
root.title("YouTube Downloader")

tk.Label(root, text="Enter YouTube URL:").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

tk.Button(root, text="Download", command=video).pack(pady=10)

root.mainloop()
