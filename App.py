import tkinter
import tkintermapview
import analyzeroute
import GMapsAPI
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
import csv
from CTkMessagebox import CTkMessagebox

import tkinter as tk

class LoginWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Login")
        label = tk.Label(self, text="Login Page")
        label.pack()

        login_button = tk.Button(self, text="Login", command=self.open_main)
        signup_button = tk.Button(self, text="Signup", command=self.open_signup)

        login_button.pack()
        signup_button.pack()

    def open_main(self):
        self.destroy()
        main_window = MainWindow()

    def open_signup(self):
        self.destroy()
        signup_window = SignupWindow()


class MainWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Main")
        label = tk.Label(self, text="Main Page")
        label.pack()

def main():
    root = ctk.CTk()
    root.title("App Start")
    login_window = LoginWindow()
    root.withdraw()  # Hide the main application window

    root.mainloop()

if __name__ == "__main__":
    main()