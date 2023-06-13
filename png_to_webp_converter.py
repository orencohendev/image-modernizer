import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from PIL import Image
from threading import Thread
import time

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Welcome to PNG Converter")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.title = tk.Label(self, text="Welcome to PNG Converter", font=("Arial", 20))
        self.title.pack(side="top")

        self.subtitle = tk.Label(self, text="Please click the Browse button to select your file", font=("Arial", 14))
        self.subtitle.pack(side="top")
        
        self.empty_line = tk.Label(self, text="")
        self.empty_line.pack(side="top")

        self.browse = tk.Button(self, text="Browse", font=("Arial", 20), height=2, width=10)
        self.browse["command"] = self.open_file_dialog
        self.browse.pack(side="top")

        self.progress = ttk.Progressbar(self, length=200, mode='indeterminate')

    def open_file_dialog(self):
        filepath = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png")])
        if filepath:
            self.progress.pack(side="bottom")
            self.progress.start()
            Thread(target=self.convert_image, args=(filepath,)).start()

    def convert_image(self, filepath):
        try:
            img = Image.open(filepath)
            time.sleep(1)  # Simulate processing time.
            self.progress.stop()
            self.progress.pack_forget()
            save_path = filedialog.asksaveasfilename(defaultextension=".webp", filetypes=[("WebP Files", "*.webp")])
            if save_path:
                img.save(save_path, "WEBP")
                print("Image converted and saved successfully.")
        except Exception as e:
            print("Error occurred while converting image: ", str(e))

def run():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    run()
