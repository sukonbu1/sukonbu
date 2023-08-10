import tkinter as tk
import tkinter.scrolledtext as tkst
import csv
import font_manager as fonts
import video_library as lib
from tkinter import filedialog
import tkinter.messagebox as msgbox
import os
from playvideos import MoviePlayer as mp


playlist_data = "Playlist_data.csv"
movie_data = "Movieplayer_data.csv"
list_all_video = []
video_playlist = []
temp_entry = []
current_hovering = []
class CreateVideoList():
    def __init__(self, window):
        window.geometry("850x400")
        window.title("Create Video List")
        window.resizable(width=False, height=False)

        enter_video_lbl = tk.Label(window, text="Enter Video ID:")
        enter_video_lbl.grid(row = 0, column = 0, sticky="E", pady=10)

        self.id_input_txt = tk.Entry(window, width=3)
        self.id_input_txt.grid(row=0, column=1, sticky='W',padx=6, columnspan=2)

        btnAdd = tk.Button(window, text="Add to playlist", command= self.add_video_btn_clicked)
        btnAdd.grid(row=0, column=2, padx=10,pady=6, sticky='e', columnspan=2)
        
        list_all_video_label = tk.Label(window, text="List of all video:")
        list_all_video_label.grid(row=1, column=0,pady=6, sticky="NE", rowspan=3)

        self.list_txt = tk.Listbox(window, width=25, height=10,activestyle='none')
        self.list_txt.grid(row=1, column=1,pady=10, sticky="NW",columnspan=3,rowspan=3)

        schrollbar = tk.Scrollbar(window)
        schrollbar.grid(row=1, column=3, sticky='nse',pady=6, rowspan=3)
        
        self.list_txt.config(yscrollcommand=schrollbar.set)
        schrollbar.config(command=self.list_txt.yview)
        
        current_list_label = tk.Label(window, text="Current list:")
        current_list_label.grid(row = 1, column = 4,sticky="NE", pady=10)

        self.playlist_txt = tk.Listbox(window, width=25, height=6,activestyle='none')
        self.playlist_txt.grid(row=1, column=5, columnspan=3,pady=10, sticky="NW")
        self.playlist_txt.bind('<<ListboxSelect>>', self.playlist_listbox_clicked)

        load_btn = tk.Button(window, text="Load", width=7, command= self.load_playlist)
        load_btn.grid(row=2, column=5,sticky='sw')

        delete_btn = tk.Button(window, text="Delete", width=11, command= self.delete_btn_clicked)
        delete_btn.grid(row=2, column=6,sticky='sw')

        play_btn = tk.Button(window, text="Play", width= 7, command=self.play_btn_clicked)
        play_btn.grid(row=3,column=5,sticky='sw')

        clear_list_btn = tk.Button(window, text="Clear Playlist", command= self.clear_list_btn_clicked)
        clear_list_btn.grid(row=3, column=6,sticky="sw")
        

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=4, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.list_of_videos()

    def add_video_btn_clicked(self):
        self.playlist_txt.configure(state = 'normal')
        key = self.id_input_txt.get()
        key = key.rjust(2, '0')
        name = lib.get_name(key)
        with open(playlist_data) as csvfile:
            readCSV = csv.reader(csvfile)
            found = False
            for column in readCSV:
                for x in column:
                    if x == name:
                        found = True
        if name in video_playlist or found or key in temp_entry:
            self.status_lbl.configure(text="Video is already in playlist!")
        elif name is not None:
            id = lib.get_id(key)
            director = lib.get_director(key)
            thumbnail = lib.get_picture(key)
            path = lib.get_moviepath(key)
            rating = lib.get_rating(key)
            temp_entry.append(key)
            video_playlist.append([id, name, director, thumbnail, path, rating])
            self.playlist_txt.insert(tk.END, name +"\n")
            self.status_lbl.configure(text="Added video to playlist")
            self.save_playlist()
        else:
            self.status_lbl.configure(text="Video not found")
        

    def load_playlist(self):
        video_playlist.clear()
        if os.path.getsize(playlist_data) == 0:
            self.status_lbl.configure(text="Playlist is empty!")
        else:
            with open (playlist_data, 'r') as f:
                lines = f.readlines()
                for row in lines:
                    movie_id = row.split(",")[0]
                    name = row.split(",")[1].strip()
                    director = row.split(",")[2].strip()
                    thumbnail = row.split(",")[3].strip()
                    path = row.split(",")[4].strip()
                    rating = row.split(",")[5].strip()
                    video_playlist.append([movie_id, name, director, thumbnail, path, rating])
            f.close()
            self.playlist_txt.configure(state = 'normal')
            self.playlist_txt.delete(0, tk.END)
            for row in video_playlist:
                self.playlist_txt.insert(tk.END,row[1] + "\n")

    def save_playlist(self):
        if len(video_playlist) == 0:
            self.status_lbl.configure(text="Current playlist is empty!")
        else:
            with open (playlist_data, 'w', newline='') as f:
                for row in video_playlist:
                    f.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]},{row[5]}\n')
                    self.status_lbl.configure(text="Playlist saved successfully!")
                f.close()

    def delete_btn_clicked(self):
        for i in range (len(video_playlist)):
            if current_hovering[0] == video_playlist[i-1]:
                video_playlist.pop(i)
                self.playlist_txt.delete(tk.ACTIVE)
                self.status_lbl.configure(text="Video removed from playlist")
                self.save_playlist()

        

    def playlist_listbox_clicked(self,event):
        current_hovering.clear()
        if self.playlist_txt.curselection() == ():
            return
        index = self.playlist_txt.curselection()[0]
        v = video_playlist[index]
        movie_id = v[0]
        name = v[1]
        director = v[2]
        thumbnail = v[3]
        path = v[4]
        rating = v[5]
        current_hovering.append([movie_id, name, director, thumbnail, path, rating])

    def play_btn_clicked(self):
        if os.path.getsize(playlist_data) == 0:
            self.status_lbl.configure(text="Playlist is empty!")
        else:
            for x in range(len(video_playlist)):
                key = video_playlist[x][0]
                lib.increment_play_count(key)
                plays = lib.get_play_count(key)
                path = lib.get_moviepath(key)
                path = lib.get_moviepath(key)
                win = tk.Toplevel()
                mp(win, path)
                # mp(tk.Toplevel(window), path)
            try:
                self.status_lbl.configure(text="Plays: " + str(plays))
            except UnboundLocalError:
                pass

    def clear_list_btn_clicked(self):
        self.playlist_txt.configure(state = 'normal')
        self.playlist_txt.delete(0 , tk.END)
        temp_entry.clear()
        video_playlist.clear()
        with open(playlist_data, 'w+') as f:
            playlist_writer = csv.writer(f)
            for row in video_playlist:
                playlist_writer.writerow(" " + "\n")
            f.close()
        self.playlist_txt.configure(state = 'disabled')
        self.status_lbl.configure(text="Playlist cleared!")

            
    def list_of_videos(self):
        with open("Movieplayer_data.csv", 'r') as all_movie_data:
            lines = all_movie_data.readlines()
            for row in lines:
                name = row.split(",")
                list_all_video.append(name)
        for row in list_all_video:
            self.list_txt.insert(tk.END,f'{row[0]}  {row[1]}') 
        all_movie_data.close()



if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    CreateVideoList(window)
    window.mainloop()