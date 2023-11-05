import tkinter
import customtkinter as tk
import tkintermapview


class StartEndBoxes(tk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.start_label = tk.CTkLabel(self, text="Start:", font=("Arial", 14))
        self.start_entry = tk.CTkEntry(self, width=200)

        self.end_label = tk.CTkLabel(self, text="End:", font=("Arial", 14))
        self.end_entry = tk.CTkEntry(self, width=200)

        self.find_button = tk.CTkButton(self, text="Find the Safest Route",
                                        command=self.find_safest_route)

        self.start_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.start_entry.grid(row=0, column=1, padx=10, pady=5)

        self.end_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.end_entry.grid(row=2, column=1, padx=10, pady=5)

        self.find_button.grid(row=3, columnspan=2, padx=10, pady=10)

    def find_safest_route(self):
        start_location = self.start_entry.get()
        end_location = self.end_entry.get()
        # Add your code to find the safest route here or perform any desired
        # action.


def main():
    root = tkinter.Tk()
    root.geometry(f"{1200}x{1000}")
    root.title("Navigation System")

    start_end_boxes = StartEndBoxes(root)
    # start_end_boxes.grid(row=0, column=0, padx=20, pady=400, sticky="n")
    start_end_boxes.pack(padx=100, pady=200, side=tkinter.LEFT)

    start_end_boxes.place(relheight=1.0, relwidth=0.25, relx=0, rely=0)

    map_widget = tkintermapview.TkinterMapView(root, width=1400, height=900,
                                               corner_radius=5)
    map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    map_widget.set_address("Toronto")

    map_widget.lower(start_end_boxes)

    root.mainloop()


if __name__ == "__main__":
    main()
