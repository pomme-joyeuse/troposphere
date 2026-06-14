from tkinter import *
from tkinter import messagebox
from pytube import YouTube
from pathlib import Path
from moviepy.editor import AudioFileClip

def au():
    url = e2.get().strip()
    destination = Path('C:/Users/noeng/Documents/Python/convert/downloads')

    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube.")
        return

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
        'quiet': False,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'noplaylist': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Audio inconnu')

        messagebox.showinfo("Succès", f"Audio téléchargé et converti : {title}.mp3")
        e2.delete(0, END)

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")