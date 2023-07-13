import os
import tkinter as tk
from tkinter import filedialog, messagebox as alert
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
        filepath = filedialog.askopenfilename(filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg"), ("JPEG Files", "*.jpeg")])
        if filepath:
            self.progress.pack(side="bottom")
            self.progress.start()
            Thread(target=self.convert_image, args=(filepath,)).start()


    def get_filename_without_extension(self, path):
        base_name = os.path.basename(path)  # Get the filename from path
        file_name_without_ext = os.path.splitext(base_name)[0]  # Get the filename without extension
        return file_name_without_ext


    def convert_image(self, filepath):
        try:
            img = Image.open(filepath)

            time.sleep(1)  # Simulate processing time.
            self.progress.stop()
            self.progress.pack_forget()
            save_path = filedialog.asksaveasfilename(initialfile=self.get_filename_without_extension(filepath),defaultextension=".webp", filetypes=[("WebP Files", "*.webp")])
            if save_path:
                img.save(save_path, "WEBP")
                alert.showinfo(title="Conversion Complete!",message="Image converted and saved successfully.")
        except Exception as e:
            alert.showerror(title="Conversion Failed!",message=f"Error occurred while converting image: {str(e)}")

def run():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()

if __name__ == '__main__':
    run()
