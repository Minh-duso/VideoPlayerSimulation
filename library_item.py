import csv

class LibraryItem:
    def __init__(self, name, director, rating=0, play_count=0, image_path=''):
        self.name = name
        self.director = director
        self.rating = rating
        self.play_count = play_count
        self.image_path = image_path

    def info(self):
        return f"{self.name}, {self.director}, Rating: {self.rating}, Plays: {self.play_count}"

    def stars(self):
        stars = ""
        for i in range(self.rating):
            stars += "*"
        return stars

video_library= {}

def get_name(video_number):
    return video_library.get(video_number, {}).get('name')

def get_director(video_number):
    return video_library.get(video_number, {}).get('director')

def get_rating(video_number):
    return video_library.get(video_number, {}).get('rating')

def get_play_count(video_number):
    return video_library.get(video_number, {}).get('play_count')

def get_image_path(video_number):
    return video_library.get(video_number, {}).get('image_path')

def list_all():
    video_list = ""
    for key, video in video_library.items():
        video_list += f"{key}: {video['name']} by {video['director']}\n"
    return video_list

def load_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            video_library[row['video_number']] = {
                'name': row['name'],
                'director': row['director'],
                'rating': int(row['rating']),
                'play_count': int(row['play_count']),
                'image_path': row.get('image_path', '')
            }