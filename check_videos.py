import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkst
from PIL import Image, ImageTk
import font_manager as fonts
import video_library as lib
from playvideos import MoviePlayer as mp
def set_text(text_area, content):    # inserts content into the text_area 
    text_area.delete("1.0", tk.END)  # first the existing content is deleted
    text_area.insert(1.0, content)   # then the new content is inserted

class CheckVideos():                            # Create a class
    def __init__(self, window):                 # Initialize 
        window.geometry("830x400")              # Set the window size
        window.title("Check Videos")            # Title of the window
        window.resizable(width=False, height=False)

        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)   # Create the "List All Videos" button bind with a function "list_videos_clicked"
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)                                         # Button's position & customizing

        self.__search_options = ["Movie ID", "Movie Name", "Director Name"]
        self.__search_option_value = tk.StringVar(window)
        self.__search_option_value.set("Movie ID")
        search_menu = tk.OptionMenu(window, self.__search_option_value, *self.__search_options)
        search_menu.grid(row=0, column=2, padx=0, pady=5)
        search_menu.config(width=13)

        enter_lbl = tk.Label(window, text="Search movie by:")       # Create a label
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)           # Positioning & Customizing 

        self.input_txt = tk.Entry(window, width=12)                  # Create an input field 
        self.input_txt.grid(row=0,sticky="W", column=3, padx=10, pady=10)      # Positioning & Design 

        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)   # Create "Check Video" button
        check_video_btn.grid(row=0, column=3,sticky="E", padx=10, pady=10)                                     # Positioning & Customizing 

        self.list_txt = tkst.ScrolledText(window, width=48, height=15, wrap="none")         # Create a Scrolled Text Field (For Video List)
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)     # Positioning & Design

        self.video_txt = tkst.ScrolledText(window, width=28, height=4, wrap="none", state = 'disable')       # Create 
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)     # Positioning & Design

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        self.play_btn = tk.Button(window, text="Play",command= self.play_btn_clicked)
        self.play_btn.grid(row=2, column=3, sticky="NE", padx=10, pady=5)

        self.thumbnail_lbl = tk.Label(window)
        self.thumbnail_lbl.grid(row=1, column=3, sticky="SW", padx=10, pady=5)       
    
    def search_option(self, choice):
        if choice == "Movie Name":  
            input_movie_name = self.input_txt.get()
            for key in lib.library:
                if input_movie_name.lower() == lib.library[key].name.lower():
                    return key
        elif choice == "Director Name":
            input_director_name = self.input_txt.get()
            for key in lib.library:
                if input_director_name.lower() == lib.library[key].director.lower():
                    return key 
        else:
            key = self.input_txt.get()
            key = key.rjust(2, '0')
            return key 

    def check_video_clicked(self):
        global path,key
        self.status_lbl.configure(state = 'normal')
        self.video_txt.configure(state = 'normal')
        choice = self.__search_option_value.get()
        key = self.search_option(choice) 
        name = lib.get_name(key)
        if name is not None:
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            picture = lib.get_picture(key)
            path = lib.get_moviepath(key)
            temp = Image.open(f'{picture}')
            video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
            set_text(self.video_txt, video_details)
            resized_image = temp.resize((250,150))
            self.__image = ImageTk.PhotoImage(resized_image)
            self.thumbnail_lbl.configure(image= self.__image)
            self.status_lbl.configure(text="Check Video button was clicked!")
            self.video_txt.configure(state= 'disabled')
        elif name is None:
            set_text(self.video_txt, f"Video not found")
            self.status_lbl.configure(text="Check Video button was clicked!")
        else:
            set_text(self.video_txt, f"Video {key} not found")
            self.status_lbl.configure(text="Check Video button was clicked!")
    def play_btn_clicked(self):
        lib.increment_play_count(key)
        win = tk.Toplevel()
        mp(win, path) 
    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list) 
        self.status_lbl.configure(text="List Videos button was clicked!")
        self.list_txt.configure(state= 'disabled')

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    CheckVideos(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
