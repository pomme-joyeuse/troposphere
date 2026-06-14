    link = input("enter url\n>> ")
    videoo = YouTube(link, 'WEB')
    ty=videoo.title
    stream = videoo.streams.get_highest_resolution()
    # check for destination to save file 
    destination = Path('C:/Users/noeng/Documents/Python/convert/downloads') 
    t = stream.download(output_path=destination)
    video = moviepy.editor.VideoFileClip(t) 
    audio = video.audio
    sound = audio.write_audiofile(ty+".mp3")
    messagebox.showinfo(ty,"downloaded !") 