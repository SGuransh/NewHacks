import tkinter
import customtkinter as tk
import tkintermapview


class StartEndBoxes(tk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.start_label = tk.CTkLabel(self, text="Start:")
        self.start_entry = tk.CTkEntry(self)

        self.end_label = tk.CTkLabel(self, text="End:")
        self.end_entry = tk.CTkEntry(self)

        self.find_button = tk.CTkButton(self, text="Find the Safest Route",
                                        command=self.find_safest_route)

        self.start_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.start_entry.grid(row=0, column=1, padx=10, pady=5)

        self.end_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.end_entry.grid(row=1, column=1, padx=10, pady=5)

        self.find_button.grid(row=2, columnspan=2, padx=10, pady=10)

    def find_safest_route(self):
        start_location = self.start_entry.get()
        end_location = self.end_entry.get()
        # Add your code to find the safest route here or perform any desired
        # action.


def main():
    root = tkinter.Tk()
    root.geometry(f"{1000}x{800}")
    root.title("Navigation System")

    start_end_boxes = StartEndBoxes(root)
    start_end_boxes.pack(padx=100, pady=100, side=tkinter.LEFT)

    map_widget = tkintermapview.TkinterMapView(root, width=1500, height=900,
                                               corner_radius=5)
    map_widget.place(relx=0.5, rely=0.5, anchor=tk.W)
    map_widget.set_address("Toronto")

    root.mainloop()


if __name__ == "__main__":
    main()
