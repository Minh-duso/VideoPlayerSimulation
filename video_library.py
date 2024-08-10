import csv
from library_item import LibraryItem

# Initialize the videos dictionary with some default data
videos = {}
    
videos["01"] = LibraryItem("Tom and Jerry", "Fred Quimby", 4);
videos["02"] = LibraryItem("Breakfast at Tiffany's", "Blake Edwards", 5);
videos["03"] = LibraryItem("Casablanca", "Michael Curtiz", 2);
videos["04"] = LibraryItem("The Sound of Music", "Robert Wise", 1);
videos["05"] = LibraryItem("Gone with the Wind", "Victor Fleming", 3);
videos["06"] = LibraryItem("Imagine", "John Lennon", 8);
videos["07"] = LibraryItem("Bohemian Rhapsody", "Queen", 7);
videos["08"] = LibraryItem("Billie Jean", "Michael Jackson", 9);
videos["09"] = LibraryItem("Stairway to Heaven", "Led Zeppelin", 6);
videos["10"] = LibraryItem("Sweet Caroline", "Neil Diamond", 10);

    

def load_from_csv(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = row['video_number']
                name = row['name']
                director = row['director']
                rating = int(row['rating'])
                play_count = int(row['play_count'])
                image_path = row.get('image_path', '')

                # Check if the key already exists in the videos dictionary
                if key in videos:
                    # Update existing entry
                    item = videos[key]
                    item.name = name
                    item.director = director
                    item.rating = rating
                    item.play_count = play_count
                    item.image_path = image_path
                else:
                    # Add new entry
                    videos[key] = LibraryItem(name, director, rating, play_count, image_path)
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def add_song_to_csv(file_path, video_number, name, director, rating, play_count, image_path):
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([video_number, name, director, rating, play_count, image_path])

def list_all():
    output = ""
    for key in videos:
        item = videos[key]
        output += f"{key} {item.info()}\n"
    return output

def get_name(video_number):
    return videos.get(video_number, {}).name

def get_director(video_number):
    return videos.get(video_number, {}).director

def get_rating(video_number):
    return videos.get(video_number, {}).rating

def set_rating(video_number, rating):
    if video_number in videos:
        videos[video_number].rating = rating

def get_play_count(video_number):
    return videos.get(video_number, {}).play_count

def increment_play_count(video_number):
    if video_number in videos:
        videos[video_number].play_count += 1

def get_image_path(video_number):
    return videos.get(video_number, {}).image_path

def search_videos_or_directors(query):
    results = []
    for key, item in videos.items():
        name = item.name.lower()
        director = item.director.lower()
        if query in name or query in director:
            results.append((key, item.name, item.director))
    return results
