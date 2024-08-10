import tkinter as tk
import tkinter.scrolledtext as tkst



import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class UpdateVideos():
    def __init__(self, window):
        window.geometry("750x350")
        window.title("Update Videos")

        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        rating_lbl = tk.Label(window, text="Rating")
        rating_lbl.grid(row=0, column=3, padx=10, pady=10)

        self.input_rating_txt = tk.Entry(window, width=3)
        self.input_rating_txt.grid(row=0, column=4, padx=10, pady=10)

        check_video_btn = tk.Button(window, text="Update videos rating", command=self.update_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        self.video_txt = tkst.ScrolledText(window, width=50, height=10)
        self.video_txt.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def update_video_clicked(self):
        key = self.input_txt.get()
        name = lib.get_name(key)
        newrating = int(self.input_rating_txt.get())
        if name is not None:
            if 1 <= newrating <= 10:
                director = lib.get_director(key)
                lib.set_rating(key, newrating)
                rating = lib.get_rating(key)
                play_count = lib.get_play_count(key)
                video_details = f"{name}\n{director}\nrating: {rating}\nplays: {play_count}"
                set_text(self.video_txt, video_details)
                self.status_lbl.configure(text="Check Video button was clicked!")
            else:
                set_text(self.video_txt, f"Rating should be between 1 and 10")
                self.status_lbl.configure(text="Check Video button was clicked!")
        else:
            self.status_lbl.configure(text = f"Video {key} not found")

    

    def list_videos_clicked(self):
        video_list = lib.list_all()
        set_text(self.list_txt, video_list)
        self.status_lbl.configure(text="List Videos button was clicked!")

if __name__ == "__main__":  # only runs when this file is run as a standalone
    window = tk.Tk()        # create a TK object
    fonts.configure()       # configure the fonts
    UpdateVideos(window)     # open the Updatevideos GUI
    window.mainloop()       # run the window main loop, reacting to button presses, etc