import customtkinter as ctk
from PIL import Image, ImageTk
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

proceed_button = ctk.CTkButton(root, text="Login", command=lambda: open_main_app())
proceed_button.pack(pady=100)

def open_main_app():
    print("Opening the main application.")

root.mainloop()