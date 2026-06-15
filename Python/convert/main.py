import tkinter as tk
from tkinter import messagebox
from video import*
from url_audio import*
from cleanning import*
from func import*
from move import*
from explorer import*
from text import*
import os
import yt_dlp
from pathlib import Path

def quit():
	MsgBox = messagebox.askquestion("Want to quit?", "Quit?")
	if MsgBox == "yes":
		fenetre.destroy()
	else:
		tk.messagebox.showinfo("Welcome Back", "Welcome back to the App")


def videooo():
    url = e1.get().strip()
    destination = 'C:/Users/noeng/Documents/Python/convert/downloads'

    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube.")
        return

    # ✅ Options yt-dlp pour ne télécharger que la vidéo du lien (pas la playlist)
    ydl_opts = {
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp3',
        'noplaylist': True,
        'quiet': False,

        # ✅ IMPORTANT FIX YT-DLP
        'cookiesfrombrowser': ('chrome', None, None, 'Noé'),
        'extractor_args': {
            'youtube': {
                'player_client': ['android']
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # extract_info permet de s'assurer qu'on ne traite qu'une vidéo
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Vidéo inconnue')

        messagebox.showinfo("Succès", f"Vidéo '{title}' téléchargée en MP4 avec succès !")
        e1.delete(0, END)

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")

def audio_mp3():
    url = e2.get().strip()
    destination = Path('C:/Users/noeng/Documents/Python/convert/downloads')

    if not url:
        messagebox.showerror("Erreur", "Veuillez entrer une URL YouTube.")
        return

    ydl_opts = {
        'outtmpl': f'{destination}/%(title)s.%(ext)s',
        'format': 'bestaudio/best',
        'noplaylist': True,
        'quiet': False,

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],

        'extractor_args': {
            'youtube': {
                'player_client': ['android']
            }
        }
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = info.get('title', 'Audio inconnu')

        messagebox.showinfo("Succès", f"Audio téléchargé et converti : {title}.mp3")
        e2.delete(0, END)

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue : {e}")



fenetre =Tk()
fenetre.title("YouTube url processing")
canvas =Canvas(fenetre, width=700, height=140, background="olive drab")
photo = PhotoImage(file="image/YouTube.PNG")
canvas.create_image(120,30, anchor=NW, image=photo)
py = PhotoImage(file="image/py.PNG")
canvas.create_image(400,30, anchor=NW, image=py)
canvas.pack()
f0=PanedWindow(fenetre, orient=HORIZONTAL, bg="gray")
f0.pack(side=TOP, expand=True, fill=X)
f0.columnconfigure(3,weight=1)
f0.rowconfigure(5,weight=1)
label = Label(f0, text='YouTube url processing', font=("Arial", 20), relief="groove", fg="black", bg="#c83012")
label.grid(column=1, row=0, sticky=N, ipadx=10, ipady=5, padx=10, pady=10)
b4=Button(f0, width=12, height=2, text="Audio",font="Arial 12 bold", relief="groove",fg="blue", bg="yellow")
b4.grid(column=0, row=1, padx=10, pady=5)
b5=Button(f0, width=12, height=2, text="Download Video",font="Arial 12 bold", relief="groove",fg="blue", bg="yellow" ,command=videooo)
b5.grid(column=1, row=1, ipadx=5, pady=5)
b8=Button(f0, width=12, height=2, text="Download mp3",font="Arial 12 bold", relief="groove",fg="blue", bg="yellow" ,command=audio_mp3)
b8.grid(column=2, row=1, ipadx=5, pady=5)
b6=Button(f0, width=12, height=2, text="cleanning",font="Arial 12 bold", relief="groove",fg="blue", bg="yellow" ,command=Clean)
b6.grid(column=2, row=3,ipadx=5, pady=5)
b7=Button(f0, width=12, height=2, text="Move",font="Arial 12 bold", relief="groove",fg="blue", bg="yellow" ,command=move)
b7.grid(column=0, row=2, ipadx=5, pady=5)
b4=Button(f0, width=12, height=2, text="Code",font="Arial 12 bold", relief="groove",fg="blue", bg="yellow" ,command=text)
b4.grid(column=0, row=3, ipadx=5, pady=5)
e1=Entry(f0, width=50, show="", relief="groove", bg="cyan")
e1.grid(column=1, row=2, ipadx=5, pady=5)
e2=Entry(f0, width=50, show="", relief="groove", bg="cyan")
e2.grid(column=2, row=2, ipadx=5, pady=5)

menubar = Menu(fenetre)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Dossier D.", command=check)
menu1.add_command(label="Editer", command=cki)
menu1.add_separator()
menu1.add_command(label="??", command=cko)
menubar.add_cascade(label="Fichier", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Quitter", command=quit)
menu2.add_command(label="New(s)", command=ck)
menu2.add_separator()
menu2.add_command(label="explorator", command=explorer)
menubar.add_cascade(label="explore", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A", command=A)
menu3.add_command(label="B", command=B)
menu3.add_command(label="C", command=C)
menu3.add_command(label="Letters", command=showletter)
menubar.add_cascade(label="Letters", menu=menu3)

fenetre.config(menu=menubar)
fenetre.mainloop()

#Need pytubefix installed wirth the command m- pip install [py module]
#Need tkinter, pathlib, os
