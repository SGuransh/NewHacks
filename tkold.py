import tkinter
import customtkinter as tk
import tkintermapview
import analyzeroute
import GMapsAPI

EXAMPLE_PATH_LIST = [(43.6608842, -79.3918635),
                     (43.6599047, -79.3908048),
                     (43.6607327, -79.38568560000002),
                     (43.660575, -79.3856169),
                     (43.660244, -79.38408679999999),
                     (43.6599447, -79.3839571),
                     (43.6597387, -79.3833956),
                     (43.6599137, -79.38262739999999),
                     (43.657374, -79.38144040000002)]


class StartEndBoxes(tk.CTkFrame):

    map_widget = None
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
        gm = GMapsAPI.GMapsAPI()

        # Comment out for testing based on actual api
        # routes = gm.getRoutes(start_location, end_location, "walking")
        # routes_formatted = gm.formatRoutes(routes)

        # Comment out when testing based on based routes
        routes_formatted = gm.SAMPLE_CRIME_HEAVY
        route_analyzer = analyzeroute.RouteAnalyzer(routes_formatted, 'major_crimes_smaller.csv')

        best_route = route_analyzer.getBestRoute()
        print(route_analyzer.relevant_crime_points)
        self.drawPath(best_route)
        self.plotCrimePoints(route_analyzer)

    def drawPath(self,  path_list: list[tuple]):
        # this code places the path and makes it zoom in and center around the path
        self.map_widget.set_position(path_list[0][0], path_list[0][1])
        self.map_widget.set_zoom(15)
        self.map_widget.set_path(path_list)

    def plotCrimePoints(self, route_analyzer: analyzeroute.RouteAnalyzer):
        self.map_widget.set_marker(43.6585663, -79.39721589999999)
        for point in route_analyzer.relevant_crime_points:
            print(point)
            print(float(point[0]))
            print(float(point[1]))
            self.map_widget.set_marker(float(point[1]), float(point[0]))



def main():
    root = tkinter.Tk()
    root.geometry(f"{1000}x{800}")
    root.title("Navigation System")

    start_end_boxes = StartEndBoxes(root)
    start_end_boxes.pack(padx=100, pady=100, side=tkinter.LEFT)


    map_widget = tkintermapview.TkinterMapView(root, width=500, height=800,
                                                    corner_radius=5)
    start_end_boxes.map_widget = map_widget
    map_widget.place(relx=0.5, rely=0.5, anchor=tk.W)
    map_widget.set_address("Toronto")


    root.mainloop()


if __name__ == "__main__":
    main()
