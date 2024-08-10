import tkinter as tk
from tkinter import messagebox, filedialog
import video_library as lib

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert("1.0", content)

class CreateVideoList:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Library Application")
        self.playlist = []

        self.video_number_label = tk.Label(root, text="Enter Video Number:")
        self.video_number_label.grid(row=0, column=0, padx=10, pady=5)

        self.video_number_entry = tk.Entry(root, width=50)
        self.video_number_entry.grid(row=0, column=1, padx=10, pady=5)

        self.add_video_button = tk.Button(root, text="Add Video", command=self.add_clicked)
        self.add_video_button.grid(row=0, column=2, padx=10, pady=5)

        self.video_listbox = tk.Listbox(root, width=50, height=10)
        self.video_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5)

        self.play_playlist_button = tk.Button(root, text="Play Playlist", command=self.play_clicked)
        self.play_playlist_button.grid(row=2, column=0, padx=10, pady=5)

        self.reset_playlist_button = tk.Button(root, text="Reset Playlist", command=self.reset_clicked)
        self.reset_playlist_button.grid(row=2, column=1, padx=10, pady=5)

        self.search_label = tk.Label(root, text="Search Name Songs:")
        self.search_label.grid(row=3, column=0, padx=10, pady=5)

        self.search_entry = tk.Entry(root, width=50)
        self.search_entry.grid(row=3, column=1, padx=10, pady=5)

        self.search_button = tk.Button(root, text="Search", command=self.search_clicked)
        self.search_button.grid(row=3, column=2, padx=10, pady=5)

        self.search_results_listbox = tk.Listbox(root, width=50, height=10)
        self.search_results_listbox.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

        self.filter_label = tk.Label(root, text="Filter by Director:")
        self.filter_label.grid(row=5, column=0, padx=10, pady=5)

        self.filter_entry = tk.Entry(root, width=50)
        self.filter_entry.grid(row=5, column=1, padx=10, pady=5)

        self.filter_button = tk.Button(root, text="Filter", command=self.filter_clicked)
        self.filter_button.grid(row=5, column=2, padx=10, pady=5)

        self.filter_results_listbox = tk.Listbox(root, width=50, height=5)
        self.filter_results_listbox.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

        self.status_label = tk.Label(root, text="Status:")
        self.status_label.grid(row=8, column=0, padx=10, pady=5)

        self.status_text = tk.Text(root, width=50, height=4)
        self.status_text.grid(row=8, column=1, columnspan=2, padx=10, pady=5)

    def reset_clicked(self):
        self.video_listbox.delete(0, tk.END)
        self.playlist.clear()
        self.status_text.insert(tk.END, "Reset playlist button was clicked!\n")

    def play_clicked(self):
        output = ""
        for key in self.playlist:
            lib.increment_play_count(key)
            name = lib.get_name(key)
            director = lib.get_director(key)
            play_count = lib.get_play_count(key)
            output += f"{name} - {director}\nPlays: {play_count}\n"
        set_text(self.status_text, output)
        self.status_text.insert(tk.END, "Play playlist button was clicked!\n")

    def list_all(self):
        output = ""
        for key in self.playlist:
            name = lib.get_name(key)
            director = lib.get_director(key)
            output += f"{name} - {director}\n"
        set_text(self.status_text, output)

    def add_clicked(self):
        key = self.video_number_entry.get()
        name = lib.get_name(key)
        director = lib.get_director(key)
        if name is not None:
            self.playlist.append(key)
            self.video_listbox.insert(tk.END, f"{name} - {director}")
            self.status_text.insert(tk.END, f"Video '{name} - {director}' added to playlist.\n")
        else:
            messagebox.showwarning("Input Error", f"Video {key} not found")
        self.status_text.insert(tk.END, "")

    def search_clicked(self):
        query = self.search_entry.get().lower()
        search_results = lib.search_videos_or_directors(query)
        self.search_results_listbox.delete(0, tk.END)
        if search_results:
            for result in search_results:
                key, name, director = result
                self.search_results_listbox.insert(tk.END, f"{key}: {name} - {director}")
        else:
            self.search_results_listbox.insert(tk.END, "No matching videos or directors found.")
        self.status_text.insert(tk.END, "Search button was clicked!\n")

    def filter_clicked(self):
        director_query = self.filter_entry.get().lower()
        self.filter_results_listbox.delete(0, tk.END)
        for key, video in lib.videos.items():
            if director_query in video.director.lower():
                self.filter_results_listbox.insert(tk.END, f"{key}: {video.name} - {video.director}")
        if not self.filter_results_listbox.size():
            self.filter_results_listbox.insert(tk.END, "No videos found for the selected director.")
        self.status_text.insert(tk.END, "Filter button was clicked!\n")

    def load_csv_clicked(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            lib.load_from_csv(file_path)
            self.status_text.insert(tk.END, "Videos loaded from CSV.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CreateVideoList(root)
    root.mainloop()
