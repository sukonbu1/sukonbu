class LibraryItem:
    def __init__(self, id, name, director, moviepicture, moviepath, rating=0):
        self.id = id
        self.name = name
        self.director = director
        self.rating = rating
        self.moviepicture = moviepicture
        self.moviepath = moviepath
        self.play_count = 0

    def info(self):
        return f"{self.name} - {self.director} {self.stars()}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars
