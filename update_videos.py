import tkinter as tk
from tkinter import *
import tkinter.scrolledtext as tkst
import pandas as pd
import font_manager as fonts
import video_library as lib
import csv
import shutil
from tkinter import filedialog
import tkinter.messagebox as msgbox

movie_data = "Movieplayer_data.csv"

video_data = []
class UpdateVideo():
    def __init__(self, window):
        window.geometry("810x400")
        window.title("Update Video")
        window.resizable(width=False, height=False)

        def list_video_data():
            with open(movie_data, 'r') as f:
                lines = f.readlines()
                global thumbnail,path
                for row in lines:
                    id = row.split(',')[0].strip()
                    name = row.split(',')[1].strip()
                    director = row.split(',')[2].strip()
                    thumbnail = row.split(',')[3].strip()
                    path = row.split(',')[4].strip()
                    rating = row.split(',')[5].strip()
                    video_data.append([id, name, director,thumbnail, path, int(rating)])
            for row in video_data:
                lstBoxAllvideo_data.insert(END, row[1])

        def save_btn_clicked():
            with open(movie_data, 'w') as f:
                for row in video_data:
                    f.write(f'{row[0]},{row[1]},{row[2]},{row[3]},{row[4]}\n')
            
            msgbox.showinfo("Save", "Data saved successfully", icon='info')

        def lstBoxAllvideo_data_clicked(event):
            if lstBoxAllvideo_data.curselection() == ():
                return
            index = lstBoxAllvideo_data.curselection()[0]
            v = video_data[index]
            id_txt.delete(0, END)
            id_txt.insert(0, v[0])
            name_txt.delete(0, END)
            name_txt.insert(0, v[1])
            director_txt.delete(0, END)
            director_txt.insert(0, v[2])
            rating_txt.delete(0, END)
            rating_txt.insert(0, v[5])

        def btnUpdate_clicked():
            if lstBoxAllvideo_data.curselection() == ():
                msgbox.showerror("Error", "Please select a video", icon='error')
                return
            
            index = lstBoxAllvideo_data.curselection()[0]  
            id, name, director, rating = get_info_textboxes()
            try:
                video_data[index] = [id, name, director,thumbnail,path, int(rating)]
                lstBoxAllvideo_data.delete(index)        
                lstBoxAllvideo_data.insert(index, name)                
                status_lbl.configure(text="Updated video information!")
            except ValueError:
                msgbox.showerror("Error", "Invalid director or rating. Please try again.", icon='error')


        def get_info_textboxes():
            id = id_txt.get()
            name = name_txt.get()   
            director = director_txt.get()      
            rating = rating_txt.get()  
            return id, name, director, rating

        def btnSearch_clicked():
            try:
                id = int(self.txtSearch.get())
                for i in range(len(video_data)):
                    if str(id) in video_data[i][0].lower():
                        lstBoxAllvideo_data.selection_clear(0, END)
                        lstBoxAllvideo_data.selection_set(i)
                        lstBoxAllvideo_data_clicked(None)
                        break
            except ValueError:
                msgbox.showerror("Error", "Invalid ID. Please try again.", icon='error')

        lblSearch = Label(window, text="Search by ID:")
        lblSearch.grid(row=0, column=0, sticky='e', pady=10)
        self.txtSearch = Entry(window)
        self.txtSearch.grid(row=0, column=1,padx=1, sticky='w', columnspan=2)

        btnSearch = Button(window, text="Search", command=btnSearch_clicked)
        btnSearch.grid(row=0, column=2, sticky='E')

        lblAllvideo_data = Label(window, text="All Movies:")
        lblAllvideo_data.grid(row=1, column=0, sticky='ne')

        lstBoxAllvideo_data = Listbox(window, width=30, height=10)
        lstBoxAllvideo_data.grid(row=1, column=1, sticky='w',padx=1, columnspan=2, rowspan=5)
        lstBoxAllvideo_data.bind('<<ListboxSelect>>', lstBoxAllvideo_data_clicked)

        schrollbar = Scrollbar(window)
        schrollbar.grid(row=1, column=3, sticky='nsew', rowspan=5)
        lstBoxAllvideo_data.config(yscrollcommand=schrollbar.set)
        schrollbar.config(command=lstBoxAllvideo_data.yview)

        id_lbl = Label(window, text="ID:")
        id_lbl.grid(row=1, column=4,sticky="ne")
        id_txt = Entry(window,width=25)
        id_txt.grid(row=1, column=5, sticky='nw',pady=5, columnspan=2)

        name_lbl = Label(window, text="Name:")
        name_lbl.grid(row=2, column=4, sticky='ne')
        name_txt = Entry(window, width=25)
        name_txt.grid(row=2, column=5, sticky='ne', pady=5,columnspan=2)

        director_lbl = Label(window, text="Director:")
        director_lbl.grid(row=3, column=4, sticky='ne')
        director_txt = Entry(window, width=25)
        director_txt.grid(row=3, column=5, sticky='ne',pady=5, columnspan=2)

        rating_lbl = Label(window, text="Rating:")
        rating_lbl.grid(row=4, column=4, sticky='ne')
        rating_txt = Entry(window, width=25)
        rating_txt.grid(row=4, column=5, sticky='ne',pady=5, columnspan=2)

        btnUpdate = Button(window, text="Update",width=7, command=btnUpdate_clicked)
        btnUpdate.grid(row=5, column=5, sticky='nw')

        btnSave = Button(window, text="Save",width=7, command=save_btn_clicked)
        btnSave.grid(row=5, column=6,sticky='ne')

        status_lbl = Label(window,text="", font=("Helvetica", 10))
        status_lbl.grid(row=6, column=0,pady=10 ,columnspan=2, sticky='sw')
        
        list_video_data()            






if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()  # create a TK object
    fonts.configure()  # configure the fonts
    UpdateVideo(window)  # open the CheckVideo GUI
    window.mainloop()  # run the window main loop, reacting to button presses, etc
