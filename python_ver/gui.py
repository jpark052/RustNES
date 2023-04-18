import tkinter as tk
import pygame.mixer as mixer
import pygame
import time, sys

class MusicPlayer:
    def __init__(self, master):
        self.master = master
        master.title("Music Player")
        master.geometry("300x150")

        self.play_button = tk.Button(master, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        self.pause_button = tk.Button(master, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=10)

        self.open_button = tk.Button(master, text="Open File", command=self.open_file)
        self.open_button.pack(pady=10)

    def open_file(self):
        # mixer.init()


        # mixer.music.load('debussy-clair-de-lune.mid')
        # mixer.music.play()
        # while mixer.music.get_busy():
        #     pygame.time.wait(1000)
        
        
        print("opening file")
        file_path = tk.filedialog.askopenfilename()
        if file_path:
            mixer.init()
            mixer.music.load(file_path)
            #mixer.music.load('debussy-clair-de-lune.mid')

            mixer.music.play()
            while mixer.music.get_busy():
                pygame.time.wait(1000)

    def play_music(self):
        mixer.music.play()

    def pause_music(self):
        mixer.music.pause()


if __name__ == '__main__':
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()