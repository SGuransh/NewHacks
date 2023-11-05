import customtkinter as ctk
from PIL import Image, ImageTk
import csv


def check_user(username, password):
    with open('users.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if len(row) >= 2 and row[0] == username and row[1] == password:
                return "Login Successful"
        return "User Error"


root = ctk.CTk()
root.title("Welcome to Your Custom App")
root.geometry("650x430")
root.iconbitmap("image_resources/logo.ico")

bg_image = Image.open("image_resources/bg2.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = ctk.CTkLabel(root, image=bg_photo, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
ctk.CTkLabel(root, text="URBAN", font=("Helvetica", 79, "bold"),
             text_color="#F08080", bg_color="#1c1a1d").pack()
label = ctk.CTkLabel(root, text="GUARDIAN", font=("Helvetica", 52),
                     text_color="white", bg_color="#1c1a1d")
label.pack()

# Create Entry widgets (text boxes)
entry1 = ctk.CTkEntry(root, width=180)
entry2 = ctk.CTkEntry(root, width=180, show="*")

# Place Entry widgets on the GUI using the pack geometry manager
entry1.pack(pady=10)
entry2.pack()

proceed_button = ctk.CTkButton(root, text="Login", command=lambda: login(),
                               width=100)
proceed_button.pack(pady=10)

# Create a button to submit the entered text
submit_button = ctk.CTkButton(root, text="Submit", command=lambda: sign_up(),
                              width=100)
submit_button.pack()


def sign_up():
    print("Opening the main application.")


def login():
    username = entry1.get()
    password = entry2.get()  # Get the entered password
    print("Login button clicked")
    result = check_user(username, password)
    if result == "Login Successful":
        print("Login Successful")
        sign_up()
        open_application(result)  # Call the main application
    elif result == "User Error":
        print("User Error")


def open_application(path):
    print(f"Opening the application at path: {path}")


root.mainloop()
