import tkinter as tk
from tkinter import ttk
from tkVideoPlayer import TkinterVideo
import datetime

class MoviePlayer():
    def __init__(self, window, video_path):
        self.window = window
        self.window.geometry('900x500')
        self.window.title("Video Player")
        self.window.resizable(width=False, height=False)

        self.video_frame = ttk.Frame(self.window)
        self.video_frame.pack()

        self.video_player = TkinterVideo(self.video_frame)
        self.video_player.pack()
        self.video_player = TkinterVideo(scaled=True, master=window)
        self.video_player.pack(expand=True, fill="both")     
        self.video_player.load(video_path)


        skip_plus_5sec = tk.Button(window, text="⏪", command=lambda: self.skip(-5))
        skip_plus_5sec.pack(side="left")

        self.play_pause_button = ttk.Button(self.window, text="▶️", command=self.play_pause)
        self.stop_button = ttk.Button(self.window, text="⏹️", command=self.stop)
        

        self.start_time = tk.Label(window, text=str(datetime.timedelta(seconds=0)))
        self.start_time.pack(side="left")

        self.play_pause_button = ttk.Button(self.window, text="▶️", command=self.play_pause)
        self.stop_button = ttk.Button(self.window, text="⏹️", command=self.stop)
        
        self.play_pause_button.pack(side=tk.LEFT, padx=5)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        self.progress_value = tk.IntVar(window)

        self.progress_slider = tk.Scale(window, variable=self.progress_value, from_=0, to=0, orient="horizontal", command=self.seek)
        # self.progress_slider.bind("<ButtonRelease-1>", self.seek)
        self.progress_slider.pack(side="left", fill="x", expand=True)

        self.end_time = tk.Label(window, text=str(datetime.timedelta(seconds=0)))
        self.end_time.pack(side="left")


        self.video_player.bind("<<Duration>>", self.update_duration)
        self.video_player.bind("<<SecondChanged>>", self.update_scale)
        self.video_player.bind("<<Ended>>", self.video_ended )


        self.skip_plus_5sec = tk.Button(window, text="⏩", command=lambda: self.skip(5))
        self.skip_plus_5sec.pack(side="left")


        self.progress_slider.config(to=0, from_=0)
        self.play_pause_button["text"] = "▶️"
        self.progress_value.set(0)

    def update_duration(self,event):
        """ updates the duration after finding the duration """
        duration = self.video_player.video_info()["duration"]
        self.end_time["text"] = str(datetime.timedelta(seconds=duration))
        self.progress_slider["to"] = duration
    

    def update_scale(self, event):
        """ updates the scale value """
        self.progress_value.set(self.video_player.current_duration())
    

    def load_internal_video(self, video_path):
        self.video_player.load(video_path)


    def seek(self,value):
        """ used to seek a specific timeframe """
        self.video_player.seek(int(value))

    def skip(self, value: int):
        """ skip seconds """
        self.video_player.seek(int(self.progress_slider.get())+value)
        self.progress_value.set(self.progress_slider.get() + value)


    def play_pause(self):
        """ pauses and plays """
        if self.video_player.is_paused():
            self.video_player.play()
            self.play_pause_button["text"] = "⏸️"

        else:
            self.video_player.pause()
            self.play_pause_button["text"] = "▶️"
    
    def video_ended(self, event):
        """ handle video ended """
        self.progress_slider.set(self.progress_slider["to"])
        self.play_pause_button["text"] = "Play"
        self.progress_slider.set(0)
    
    def stop(self):
        self.video_player.stop()
    




if __name__ == "__main__":
    window = tk.Tk()
    app = (MoviePlayer(window,video_path='videosdata/Rickroll.mp4'))

    # Set the video path internally and load the video

    window.mainloop()


