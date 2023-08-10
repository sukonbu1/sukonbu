import tkinter as tk
import font_manager as fonts
from check_videos import CheckVideos
from create_video_list import CreateVideoList
from update_videos import UpdateVideo
class VideoPlayer():
    def __init__(self,window):
        window.geometry("520x150")
        window.title("Video Player")
        window.resizable(width=False, height=False)

        header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
        header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        check_videos_btn = tk.Button(window, text="Check Videos", command=self.check_videos_clicked)
        check_videos_btn.grid(row=1, column=0, padx=10, pady=10)

        create_video_list_btn = tk.Button(window, text="Create Video List", command=self.create_video_list_clicked)
        create_video_list_btn.grid(row=1, column=1, padx=10, pady=10)

        update_videos_btn = tk.Button(window, text="Update Videos", command=self.update_video_clicked)
        update_videos_btn.grid(row=1, column=2, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    def check_videos_clicked(self):
        self.status_lbl.configure(text="Check Videos button was clicked!")
        CheckVideos(tk.Toplevel(window))

    def create_video_list_clicked(self):
        self.status_lbl.configure(text="Create video list button was clicked!")
        CreateVideoList(tk.Toplevel(window))

    def update_video_clicked(self):
        self.status_lbl.configure(text="Update Video button was clicked!")
        UpdateVideo(tk.Toplevel(window))


if __name__ == "__main__":
    window = tk.Tk()
    fonts.configure()
    VideoPlayer(window)
    window.mainloop()
