import tkinter
import tkintermapview
import analyzeroute
import GMapsAPI
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog

import tkinter as tk

class Frame1(tk.Frame):
    def __init__(self, master, switch_to_frame):
        super().__init__(master)
        self.switch_to_frame = switch_to_frame
        label = tk.Label(self, text="This is Frame 1")
        label.pack()
        button = tk.Button(self, text="Switch to Frame 2", command=lambda: self.switch_to_frame(2))
        button.pack()

class Frame2(tk.Frame):
    def __init__(self, master, switch_to_frame):
        super().__init__(master)
        self.switch_to_frame = switch_to_frame
        label = tk.Label(self, text="This is Frame 2")
        label.pack()
        button = tk.Button(self, text="Switch to Frame 3", command=lambda: self.switch_to_frame(3))
        button.pack()

class Frame3(tk.Frame):
    def __init__(self, master, switch_to_frame):
        super().__init__(master)
        self.switch_to_frame = switch_to_frame
        label = tk.Label(self, text="This is Frame 3")
        label.pack()
        button = tk.Button(self, text="Switch to Frame 1", command=lambda: self.switch_to_frame(1))
        button.pack()

class MainApp(tk.Tk):
    frames = {}

    def __init__(self):
        super().__init__()
        self.title("Switching Frames Example")
        self.geometry("400x300")
        self.current_frame = None

        MainApp.frames[1] = Frame1(self, self.switch_to_frame)
        MainApp.frames[2] = Frame2(self, self.switch_to_frame)
        MainApp.frames[3] = Frame3(self, self.switch_to_frame)

        self.switch_to_frame(1)

    def switch_to_frame(self, frame_number):
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = MainApp.frames[frame_number]
        self.current_frame.pack()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

