import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import filedialog

root = ctk.CTk()
root.title("Welcome to Your Custom App")
root.geometry("650x430")
root.iconbitmap("image_resources/logo.ico")

bg_image = Image.open("image_resources/bg2.jpeg")
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = ctk.CTkLabel(root, image=bg_photo, text="")
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
ctk.CTkLabel(root, text="URBAN", font=("Helvetica", 79, "bold"), text_color="#F08080", bg_color="#1c1a1d").pack()
label = ctk.CTkLabel(root, text="GUARDIAN", font=("Helvetica", 52), text_color="white", bg_color="#1c1a1d")
label.pack()

entry1 = ctk.CTkEntry(root, width=180)
entry2 = ctk.CTkEntry(root, width=180)
entry3 = ctk.CTkEntry(root, width=180)

# Place Entry widgets on the GUI using the pack geometry manager
entry1.pack(pady=10)
entry2.pack()
entry3.pack(pady=10)

pdf_upload = ctk.CTkButton(root, text="Upload schedule", command=lambda: open_file_dialog())
pdf_upload.pack(pady=10)

proceed_button = ctk.CTkButton(root, text="Signup", command=lambda: open_main_app())
proceed_button.pack(pady=10)


def open_main_app():
    print("Opening the main application.")


def open_file_dialog():
    filename = filedialog.askopenfilename(initialdir="/gui/images", title="Choose the timetable", filetypes=(("pdf files", "*.pdf"), ("all files", "*.pdf")))
    if filename:
        # Do something with the selected file path (e.g., open and read the file)
        print(f"Selected file: {filename}")


root.mainloop()
