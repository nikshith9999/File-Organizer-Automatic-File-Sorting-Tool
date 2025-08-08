import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    path = filedialog.askdirectory(title="Select Folder to Organize")
    if not path:
        return

    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get file extension (without dot)
        filename, extension = os.path.splitext(file)
        extension = extension[1:].lower()
        if not extension:
            continue

        # Get file's year of creation/modification
        year = time.strftime('%Y', time.localtime(os.path.getmtime(file_path)))

        # Create year folder
        year_folder = os.path.join(path, year)
        os.makedirs(year_folder, exist_ok=True)

        # Create extension/category folder inside year folder
        ext_folder = os.path.join(year_folder, extension)
        os.makedirs(ext_folder, exist_ok=True)

        # Move file into year -> extension folder
        shutil.move(file_path, os.path.join(ext_folder, file))

    messagebox.showinfo("Done", "✅ Files organized by Year and Extension!")

# ---------------- GUI Part---------------- #
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")
root.configure(bg="lightblue")

tk.Label(root, text="Organize Files by Year & Extension", bg="lightblue", font=("Arial", 12, "bold")).pack(pady=15)

tk.Button(root, text="Choose Folder & Organize", command=organize_files, width=25, height=2, bg="white").pack(pady=10)

tk.Button(root, text="Exit", command=root.destroy, width=25, height=1, bg="white").pack(pady=5)

root.mainloop()
