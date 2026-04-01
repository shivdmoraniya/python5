import tkinter as tk
from tkinter import filedialog
import os
import sys
import subprocess

def open_video():
    filepath = filedialog.askopenfilename(
        title="Select a Video File",
        filetypes=[
            ("Video files", "*.mp4 *.avi *.mkv *.mov *.flv *.wmv"),
            ("All files", "*.*")
        ]
    )
    if filepath:
        try:
            if sys.platform == "win32":
                os.startfile(filepath)
            elif sys.platform == "darwin": # macOS
                subprocess.Popen(["open", filepath])
            else: # Linux and other Unix-like systems
                subprocess.Popen(["xdg-open", filepath])
        except Exception as e:
            print(f"Error opening video: {e}")
            tk.messagebox.showerror("Error", f"Could not open video: {e}")

root = tk.Tk()
root.title("Simple Video Opener")

window_width = 400
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (window_width / 2)
y = (screen_height / 2) - (window_height / 2)
root.geometry(f'{window_width}x{window_height}+{int(x)}+{int(y)}')

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True, fill='both')

label = tk.Label(frame, text="Click the button to open a video file.")
label.pack(pady=10)

open_button = tk.Button(frame, text="Open Video", command=open_video)
open_button.pack(pady=10)

root.mainloop()