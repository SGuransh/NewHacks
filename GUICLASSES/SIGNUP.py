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


class SignupWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Signup")
        self.cr = 5
        label = tk.Label(self, text="Signup Page")
        label.pack()

        # back_button = tk.Button(self, text="Back to Login", command=self.open_login)
        # signup_button = tk.Button(self, text="Signup", command=self.open_main)
        # back_button.pack()
        # signup_button.pack()

        self.title("Welcome to Your Custom App")
        self.geometry("1000x800")
        self.iconbitmap("C:/Users/sgura/PycharmProjects/NewHacks/image_resources/logo.ico")

        self.bg_image = Image.open("C:/Users/sgura/PycharmProjects/NewHacks/image_resources/bg2.jpeg")
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = ctk.CTkLabel(self, image=self.bg_photo, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        ctk.CTkLabel(self, text="URBAN", font=("Helvetica", 79, "bold"),
                     text_color="#F08080", bg_color="#1c1a1d").pack()
        label = ctk.CTkLabel(self, text="GUARDIAN", font=("Helvetica", 52),
                             text_color="white", bg_color="#1c1a1d")
        label.pack()

        self.entry1 = ctk.CTkEntry(self, width=180, corner_radius=self.cr, bg_color="#1c1a1d")
        self.entry1.insert(0, "Enter the Username")
        self.first1 = True
        self.entry2 = ctk.CTkEntry(self, width=180, corner_radius=self.cr, bg_color="#1c1a1d")
        self.entry2.insert(0, "Enter Password")
        self.first2 = True
        self.entry3 = ctk.CTkEntry(self, width=180, corner_radius=self.cr, bg_color="#1c1a1d")
        self.entry3.insert(0, "Re enter the password")
        self.first3 = True

        # Place Entry widgets on the GUI using the pack geometry manager
        self.entry1.pack(pady=10)
        self.entry1.bind("<FocusIn>", self.on_entry_click1)
        self.entry2.pack()
        self.entry2.bind("<FocusIn>", self.on_entry_click2)
        self.entry3.pack(pady=10)
        self.entry3.bind("<FocusIn>", self.on_entry_click3)

        pdf_upload = ctk.CTkButton(self, text="Upload schedule",
                                   command=lambda: self.open_file_dialog(), corner_radius=self.cr, bg_color="#1c1a1d")
        pdf_upload.pack(pady=10)

        proceed_button = ctk.CTkButton(self, text="Signup",
                                       command=lambda: self.sign_up_activate(), corner_radius=self.cr, bg_color="#1c1a1d")
        proceed_button.pack(pady=10)

    def on_entry_click1(self, event):
        if self.first1:
            self.entry1.delete(0, "end")

    def on_entry_click2(self, event):
        if self.first2:
            self.entry2.delete(0, "end")
            self.entry2.configure(show="*")

    def on_entry_click3(self, event):
        if self.first3:
            self.entry3.delete(0, "end")
            self.entry3.configure(show="*")

    def check_password(self, pass1, pass2) -> bool:
        if pass1 != pass2:
            CTkMessagebox(title="Error", message="Passwords Don't Match!!!",
                          icon="cancel")
            self.entry2.delete(0, "end")
            self.entry3.delete(0, "end")
            return False

    def check_username(self, username) -> bool:
        with open("Users/users.csv", "r") as file:
            reader = csv.reader(file)
            for i in reader:
                if len(i) > 1 and i[0] == username:
                    CTkMessagebox(title="Error",
                                  message="Username Not Available!!!",
                                  icon="cancel")
                    self.entry1.delete(0, "end")
            return False

    def save_user(self, username, password):
        with open("Users/users.csv", "a") as file:
            writer = csv.writer(file)
            try:
                line = [username, password, filename]
            except NameError:
                line = [username, password, ""]
            writer.writerow(line)
            self.CTkMessagebox(message=f"{username} has been created!!!",
                          icon="check", option_1="Thanks")
            self.entry3.delete(0, "end")
            self.entry1.delete(0, "end")
            self.entry2.delete(0, "end")
            # Open the login page
            self.destroy()
            # login_window = LoginWindow()

    def sign_up_activate(self):
        good_to_go = True
        username = self.entry1.get()
        password = self.entry2.get()
        repeat = self.entry3.get()
        good_to_go = self.check_password(password, repeat)
        if good_to_go:
            good_to_go = self.check_username(username)
            if good_to_go:
                self.save_user(username, password)

    def open_file_dialog(self):
        global filename
        data_lost = self.entry3.get()
        filename = filedialog.askopenfilename(initialdir="/gui/images",
                                              title="Choose the timetable",
                                              filetypes=(("pdf files", "*.pdf"),
                                                         ("all files", "*.pdf")))
        if filename:
            # Do something with the selected file path (e.g., open and read the
            # file)
            print(f"Selected file: {filename}")
        self.entry3.insert(0, data_lost)

    # def open_login(self):
    #     self.destroy()
    #     login_window = LoginWindow()

    # def open_main(self):
    #     self.destroy()
    #     main_window = MainWindow()

if __name__ == "__main__":
    root = ctk.CTk()
    SignupWindow = SignupWindow()
    root.withdraw()
    root.mainloop()