import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
import csv


def on_entry_click1(event):
    if first1:
        entry1.delete(0, "end")


def on_entry_click2(event):
    if first2:
        entry2.delete(0, "end")
        entry2.configure(show="*")


def on_entry_click3(event):
    if first3:
        entry3.delete(0, "end")
        entry3.configure(show="*")


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

entry1 = ctk.CTkEntry(root, width=180)
entry1.insert(0, "Enter the Username")
first1 = True
entry2 = ctk.CTkEntry(root, width=180)
entry2.insert(0, "Enter Password")
first2 = True
entry3 = ctk.CTkEntry(root, width=180)
entry3.insert(0, "Re enter the password")
first3 = True

# Place Entry widgets on the GUI using the pack geometry manager
entry1.pack(pady=10)
entry1.bind("<FocusIn>", on_entry_click1)
entry2.pack()
entry2.bind("<FocusIn>", on_entry_click2)
entry3.pack(pady=10)
entry3.bind("<FocusIn>", on_entry_click3)

pdf_upload = ctk.CTkButton(root, text="Upload schedule",
                           command=lambda: open_file_dialog())
pdf_upload.pack(pady=10)

proceed_button = ctk.CTkButton(root, text="Signup",
                               command=lambda: sign_up_activate())
proceed_button.pack(pady=10)


def check_password(pass1, pass2):
    if pass1 != pass2:
        CTkMessagebox(title="Error", message="Passwords Don't Match!!!",
                      icon="cancel")
        entry2.delete(0, "end")
        entry3.delete(0, "end")


def check_username(username):
    with open("Users/users.csv", "r") as file:
        reader = csv.reader(file)
        for i in reader:
            if len(i) > 1 and i[0] == username:
                CTkMessagebox(title="Error",
                              message="Username Not Available!!!",
                              icon="cancel")
                entry1.delete(0, "end")
        good_to_go = False


def save_user(username, password):
    with open("Users/users.csv", "a") as file:
        writer = csv.writer(file)
        try:
            line = [username, password, filename]
        except NameError:
            line = [username, password, ""]
        writer.writerow(line)
        CTkMessagebox(message=f"{username} has been created!!!",
                      icon="check", option_1="Thanks")
        good_to_go = False
        entry3.delete(0, "end")
        entry1.delete(0, "end")
        entry2.delete(0, "end")
        # Open the login page


def sign_up_activate():
    global good_to_go
    good_to_go = True
    username = entry1.get()
    password = entry2.get()
    repeat = entry3.get()
    check_password(password, repeat)
    check_username(username)
    if good_to_go:
        save_user(username, password)


def open_file_dialog():
    global filename
    data_lost = entry3.get()
    filename = filedialog.askopenfilename(initialdir="/gui/images",
                                          title="Choose the timetable",
                                          filetypes=(("pdf files", "*.pdf"),
                                                     ("all files", "*.pdf")))
    if filename:
        # Do something with the selected file path (e.g., open and read the file)
        print(f"Selected file: {filename}")
    entry3.insert(0, data_lost)


root.mainloop()
