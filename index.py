from pytube import YouTube
from moviepy.editor import *
import tkinter as tk
from tkinter import messagebox

def baixar_audio():
    url = url_entry.get()
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        video.download()
        mp4_file = video.default_filename
        mp3_file = mp4_file.split(".mp4")[0] + ".mp3"
        video_clip = AudioFileClip(mp4_file)
        video_clip.write_audiofile(mp3_file)
        video_clip.close()
        messagebox.showinfo("Conversão completa", "O áudio foi baixado com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

# Interface gráfica
root = tk.Tk()
root.title("Conversor de Vídeo para Áudio")

url_label = tk.Label(root, text="URL do vídeo:")
url_label.pack()

url_entry = tk.Entry(root, width=50)
url_entry.pack()

converter_button = tk.Button(root, text="Converter para Áudio", command=baixar_audio)
converter_button.pack()

root.mainloop()
