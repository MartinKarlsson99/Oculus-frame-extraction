import os
import tkinter as tk
from tkinter import filedialog, ttk

import cv2

from video_tools import chop_video, apply_mask
from mask import get_mask


def mask_images(frames, output_dir, mask, p_bar):
    for frame in frames:
        img = cv2.imread(os.path.join(output_dir, frame))
        img = apply_mask(img, mask)
        cv2.imwrite(os.path.join(output_dir, frame), img)
        p_bar.step()
        root.update()


def select_avi_file():
    file_path = filedialog.askopenfilename(filetypes=[("AVI files", "*.avi")])
    avi_path_var.set(file_path)


def select_output_directory():
    directory = filedialog.askdirectory()
    output_dir_var.set(directory)


def confirm_selection():
    confirm_button.destroy()
    label = tk.Label(root, text='Chopping video...')
    label.grid(row=2, column=0, columnspan=3, pady=10)
    root.update()

    # Processing
    chop_video(avi_path_var.get(), output_dir_var.get())
    label.destroy()
    label = tk.Label(root, text='Applying masks...')
    label.grid(row=2, column=0, columnspan=3, pady=10)


    frames = os.listdir(output_dir_var.get())
    p_bar = tk.ttk.Progressbar(root, orient='horizontal', length=300, mode='determinate', maximum=len(frames))
    p_bar.grid(row=3, column=0, columnspan=3, pady=10)

    root.update()

    mask = get_mask()
    mask_images(frames, output_dir_var.get(), mask, p_bar)

    root.destroy()

root = tk.Tk()
root.title('Sonar Frame Converter')

avi_path_var = tk.StringVar()
output_dir_var = tk.StringVar()

tk.Label(root, text="AVI File:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=avi_path_var, width=50).grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_avi_file).grid(row=0, column=2, padx=5, pady=5)

tk.Label(root, text="Output Directory:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="Browse", command=select_output_directory).grid(row=1, column=2, padx=5, pady=5)

confirm_button = tk.Button(root, text="Confirm", command=confirm_selection)
confirm_button.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()