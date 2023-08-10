from library_item import LibraryItem
from PIL import ImageTk, Image
import csv
import pandas as pd
filename = r"C:\Users\Administrator\Desktop\VideoPlayer2\Movieplayer_data.csv"
file = pd.read_csv(filename)
# initializing the titles and rows list
data = []
fields = []
movies = []
with open(filename, 'r') as f:
    lines = f.readlines()
    for row in lines:
        id = row.split(',')[0].strip()
        name = row.split(',')[1].strip()
        director = row.split(',')[2].strip()
        thumbnail =row.split(',')[3].strip()
        path = row.split(',')[4].strip()
        rating = row.split(',')[5].strip()
        movies.append([id, name, director, thumbnail, path, rating])
        
library = {}
library["01"] = LibraryItem(movies[0][0], movies[0][1], movies[0][2], movies[0][3], movies[0][4], int(movies[0][5]))
library["02"] = LibraryItem(movies[1][0], movies[1][1], movies[1][2], movies[1][3], movies[1][4], int(movies[1][5]))
library["03"] = LibraryItem(movies[2][0], movies[2][1], movies[2][2], movies[2][3], movies[2][4], int(movies[2][5]))
library["04"] = LibraryItem(movies[3][0], movies[3][1], movies[3][2], movies[3][3], movies[3][4], int(movies[3][5]))
library["05"] = LibraryItem(movies[4][0], movies[4][1], movies[4][2], movies[4][3], movies[4][4], int(movies[4][5]))

def list_all():
    output = ""
    for key in library:
        item = library[key]
        output += f"{key} {item.info()}\n"
    return output

def get_id(key):
    try:
        item = library[key]
        return str(item.id)
    except KeyError:
        return None

def get_name(key):
    try:
        item = library[key]
        return item.name
    except KeyError:
        return None

def get_director(key):
    try:
        item = library[key]
        return item.director
    except KeyError:
        return None


def get_rating(key):
    try:
        item = library[key]
        return item.rating
    except KeyError:
        return -1

def get_picture(key):
    try:
        item = library[key]
        return item.moviepicture
    except KeyError:
        return None

def get_moviepath(key):
    try:
        item = library[key]
        return item.moviepath
    except KeyError:
        return None

def set_rating(key, rating):
    try:
        item = library[key]
        item.rating = rating
        file.loc[int(key)-1,'Rating'] = rating
    except KeyError:
        return

def get_play_count(key):
    try:
        item = library[key]
        return item.play_count
    except KeyError:
        return -1

def increment_play_count(key):
    try:
        item = library[key]
        item.play_count += 1
        file.loc[int(key)-1,'Play Count'] = item.play_count
    except KeyError:
        return