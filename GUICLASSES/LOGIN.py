import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
import csv
class LoginWindow(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Login")
        self.geometry("650x430")
        self.iconbitmap("image_resources/logo.ico")
        bg_image = Image.open("image_resources/bg2.jpeg")
        bg_photo = ImageTk.PhotoImage(bg_image)

        bg_label = ctk.CTkLabel(self, image=bg_photo, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        ctk.CTkLabel(self, text="URBAN", font=("Helvetica", 79, "bold"),
                     text_color="#F08080", bg_color="#1c1a1d").pack()
        label = ctk.CTkLabel(self, text="GUARDIAN", font=("Helvetica", 52),
                             text_color="white", bg_color="#1c1a1d")
        label.pack()

        login_button = tk.Button(self, text="Login", command=self.open_main)
        signup_button = tk.Button(self, text="Signup", command=self.open_signup)

        login_button.pack()
        signup_button.pack()

    # def open_main(self):
    #     self.destroy()
    #     main_window = MainWindow()
    #
    # def open_signup(self):
    #     self.destroy()
    #     signup_window = SignupWindow()



    # Create Entry widgets (text boxes)
        self.entry1 = ctk.CTkEntry(self, width=180)
        self.entry2 = ctk.CTkEntry(self, width=180, show="*")

        # Place Entry widgets on the GUI using the pack geometry manager
        self.entry1.pack(pady=10)
        self.entry2.pack()

        proceed_button = ctk.CTkButton(self, text="Login", command=lambda: self.login(),
                                       width=100)
        proceed_button.pack(pady=10)

        # Create a button to submit the entered text
        submit_button = ctk.CTkButton(self, text="Submit", command=lambda: self.sign_up(),
                                      width=100)
        submit_button.pack()

    def check_user(self, username, password) -> tuple:
        with open("Users/users.csv", 'r') as file:
            reader = csv.reader(file)
            for i in reader:
                if len(i) > 1 and i[0] == username and i[1] == password:
                    return i[2], "Login Successful"
            return "", "User Error"

    def sign_up(self):
        print("Opening the main application.")


    def login(self):
        username = self.entry1.get()
        password = self.entry2.get()  # Get the entered password
        print("Login button clicked")
        filename, result = self.check_user(username, password)
        if result == "Login Successful":
            print("Login Successful")
            self.sign_up()
            if filename:
                print("Filepath:", filename)
        elif result == "User Error":
            print("User Error")
