import customtkinter as ctk
from PIL import Image, ImageTk

root = ctk.CTk()
root.title("Welcome to Your Custom App")
root.geometry("1450x900")
root.iconbitmap("image_resources/logo.ico")
# ctk.set_default_color_theme("Dark")
# # bg_image = Image.open("background.jpg")  # Replace "background.jpg" with your image file
# # bg_photo = ImageTk.PhotoImage(bg_image)
# #
# # bg_label = ctk.CTkLabel(root, image=bg_photo)
# #
# # bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Fill the entire window with the image

welcome_label = ctk.CTkLabel(root, text="URBAN", font=("Helvetica", 52, "bold"), text_color="#F08080").pack()
ctk.CTkLabel(root, text="GUARDIAN", font=("Helvetica", 32), text_color="white").pack()

my_image = ctk.CTkImage(light_image=Image.open("image_resources/front_person.png"),
                                  dark_image=Image.open("image_resources/front_person.png"),
                                  size=(40, 60))

image_label = ctk.CTkLabel(root, image=my_image, text="").pack()

proceed_button = ctk.CTkButton(root, text="Proceed", command=lambda: open_main_app())
proceed_button.pack()

def open_main_app():
    print("Opening the main application.")

root.mainloop()