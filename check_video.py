import tkinter as tk  # Importing the tkinter module for GUI creation
import tkinter.scrolledtext as tkst  # Importing the scrolledtext module for text widgets with a scrollbar
import video_library as lib  # Importing a custom video library module
import font_manager as fonts  # Importing a custom font manager module
from tkinter import filedialog
from PIL import Image, ImageTk

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Delete all current content in the text area
    text_area.insert(1.0, content)  # Insert the new content into the text area

class CheckVideos():
    def __init__(self, window):
        window.geometry("1000x600")  # Set the window size (increased height for image display)
        window.title("Check Videos")  # Set the window title

        # Button to list all videos
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  # Position the button in the grid

        # Label for the video number input
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  # Position the label in the grid

        # Text entry for the video number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)  # Position the text entry in the grid

        # Button to check the details of a video
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  # Position the button in the grid

        load_csv_btn = tk.Button(window, text="Load More Songs from CSV", command=self.load_csv_clicked)
        load_csv_btn.grid(row=0, column=4, padx=10, pady=10)

        # Scrolled text area to list all videos
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  # Position the text area in the grid

        # Text area to display video details
        self.video_txt = tk.Text(window, width=24, height=8, wrap="none")
        self.video_txt.grid(row=1, column=3, columnspan=2, sticky="NW", padx=10, pady=10)  # Position the text area in the grid

        # Image label to display the video image
        self.image_lbl = tk.Label(window)
        self.image_lbl.grid(row=2, column=3, padx=10, pady=10)  # Position the image label in the grid

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)  # Position the label in the grid

        set_text(self.list_txt, "")
        
    def check_video_clicked(self):
        key = self.input_txt.get()  # Get the video number from the input text
        name = lib.get_name(key)  # Get the video name using the library function
        if name is not None:
            director = lib.get_director(key)  # Get the video director
            rating = lib.get_rating(key)  # Get the video rating
            play_count = lib.get_play_count(key)  # Get the video play count
            video_details = f"Video Number: {key}\nName: {name}\nDirector: {director}\nRating: {rating}\nPlay Count: {play_count}"  # Format the video details
            set_text(self.video_txt, video_details)  # Set the video details in the text area

            image_path = lib.get_image_path(key)  # Add this function to your video_library module
            if image_path:
                image = Image.open(image_path)
                image = image.resize((500, 250), Image.LANCZOS)  # Resize the image to fit the label
                photo = ImageTk.PhotoImage(image)
                self.image_lbl.configure(image=photo)
                self.image_lbl.image = photo  # Keep a reference to the image to prevent garbage collection
            else:
                self.image_lbl.configure(image='')
                self.image_lbl.image = None
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Display not found message
            self.image_lbl.configure(image='')
            self.image_lbl.image = None
        self.status_lbl.configure(text="Check Video button was clicked!")  # Update the status label

    def list_videos_clicked(self):
        video_list = lib.list_all()  # Get the list of all videos
        set_text(self.list_txt, video_list)  # Set the video list in the scrolled text area
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status label

    def load_csv_clicked(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            lib.load_from_csv(file_path)
            self.list_videos_clicked()  # Refresh the list after loading CSV
            self.status_lbl.configure(text="Load More Songs from CSV button was clicked!")

if __name__ == "__main__":  # Only runs when this file is run as a standalone script
    window = tk.Tk()  # Create a TK object
    fonts.configure()  # Configure the fonts using the font manager module
    app = CheckVideos(window)  # Open the CheckVideos GUI
    window.mainloop()  # Run the window main loop, reacting to button presses, etc.
