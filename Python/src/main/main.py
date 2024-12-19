import os
import tkinter as tk
from tkinter import filedialog

from PIL import Image

print(Image.__version__)

player_skin_file_path = filedialog.askopenfilename(filetypes=[(".png", "*.png")], initialdir=os.path.abspath(os.path.dirname(__file__)))

with open(file=player_skin_file_path, mode="r") as f:
    print(f.read())