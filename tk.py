import datetime
import tkinter

import customtkinter
import customtkinter as tk
import tkintermapview
import analyzeroute
import GMapsAPI
import timetable_parser

UOFT_BUILDING_CODES = {"EM": "75 Queen's Park Cres E, Toronto, ON M5S 1K7",
                       "MP": "McLennan Physical Laboratories, 255 Huron St, Toronto, ON M5S 1A7",
                       "BF": "4 Bancroft Ave, Toronto, ON M5S 1C1",
                       "CR": "100 St Joseph St, Toronto, ON M5S 2C4",
                       "BL": "Claude T. Bissell Building, 140 St George St, Toronto, ON M5S 3G6",
                       "MS": "Medical Sciences Building, 1 King's College Cir, Toronto, ON M5S 1A8",
                       "NF": "Toronto, ON M5S 1K6",
                       "RW": "Toronto, ON M5S 3G5",
                       "OI": "252 Bloor St W, Toronto, ON M5S 1V6",
                       "MY": "55 St George St, Toronto, ON M5S 0C9",
                       "UC": "University College (Main Building), 15 King's College Cir, Toronto, ON M5S 3H7",
                       "NL": "6 Queens Pk Cres W, Toronto, ON M5S 3H2",
                       "SK": "Factor-Inwentash Faculty of Social Work, 246 Bloor St W, Toronto, ON M5S 1V4"}



class StartEndBoxes(tk.CTkFrame):
    map_widget = None
    syllabus_pdf = None
    user_choice = None
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


        self.setupDropDown()
        self.fakeLabel = tk.CTkLabel(self, text='TODAY IS '+ self.day.upper()).grid(row=6, columnspan=2)
        self.days_dropdown.grid(row=7, columnspan=2)
        self.fakeLabel = tk.CTkLabel(self, text='').grid(row=8,
                                                                                     columnspan=2)
        self.find_button = tk.CTkButton(self, text="Go To Class",
                                        command=self.findSafestRouteToClass).grid(row=9, columnspan=2)

    def setupDropDown(self):
        self.week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Friday', 'Friday']
        self.day = self.week[datetime.datetime.now().weekday()]
        parser = timetable_parser.Parser(self.getPdfFilePath())

        courses_of_today = []

        for lecture in parser.days_dict[self.day]:
            courses_of_today.append(lecture + ' - ' + parser.days_dict[self.day][lecture])

        self.days_dropdown = tk.CTkComboBox(self, values=courses_of_today, command=self.combobox_callback)
        self.fakeLabel = tk.CTkLabel(self, text='').grid(row=4)
        self.fakeLabel = tk.CTkLabel(self, text='').grid(row=5)

    def findSafestRouteToClass(self):
        start_location = self.start_entry.get()
        gm = GMapsAPI.GMapsAPI()

        # Comment out for testing based on actual api
        routes = gm.getRoutes(start_location, UOFT_BUILDING_CODES[self.user_choice], "walking")
        start_location = routes[0]["legs"][0]["start_location"]
        routes_formatted = gm.formatRoutes(routes)

        # routes = gm.SAMPLE_SPADINA_STGEORGE
        # start_location = routes[0]["legs"][0]["start_location"]
        # routes_formatted = gm.formatRoutes(routes)

        # Comment out when testing based on based routes
        # routes_formatted = gm.SAMPLE_CRIME_HEAVY
        route_analyzer = analyzeroute.RouteAnalyzer(routes_formatted, 'major_crimes_smaller.csv')

        best_route = route_analyzer.getBestRoute()
        self.drawPath(start_location, best_route)
        self.plotCrimePoints(route_analyzer)


    def combobox_callback(self, choice:str):
        user_choice = choice.split(' ')[-2]
        print(user_choice)
        self.user_choice = user_choice

    def find_safest_route(self):
        start_location = self.start_entry.get()
        end_location = self.end_entry.get()
        # Add your code to find the safest route here or perform any desired
        # action.
        gm = GMapsAPI.GMapsAPI()

        # Comment out for testing based on actual api
        routes = gm.getRoutes(start_location, end_location, "walking")
        start_location = routes["legs"]["start_location"]
        routes_formatted = gm.formatRoutes(routes)

        # routes = gm.SAMPLE_SPADINA_STGEORGE
        # start_location = routes[0]["legs"][0]["start_location"]
        # routes_formatted = gm.formatRoutes(routes)

        # Comment out when testing based on based routes
        # routes_formatted = gm.SAMPLE_CRIME_HEAVY
        route_analyzer = analyzeroute.RouteAnalyzer(routes_formatted, 'major_crimes_smaller.csv')

        best_route = route_analyzer.getBestRoute()
        self.drawPath(start_location, best_route)
        self.plotCrimePoints(route_analyzer)

    def drawPath(self, start_location: dict, path_list: list[tuple]):
        print(start_location)
        # this code places the path and makes it zoom in and center around the path
        path_list.insert(0, (start_location["lat"], start_location["lng"]))
        self.map_widget.set_position(path_list[0][0], path_list[0][1])
        self.map_widget.set_zoom(15)
        self.map_widget.set_path(path_list)

    def plotCrimePoints(self, route_analyzer: analyzeroute.RouteAnalyzer):
        self.map_widget.set_marker(43.6585663, -79.39721589999999)
        for point in route_analyzer.relevant_crime_points:
            self.map_widget.set_marker(float(point[1]), float(point[0]))


    def login(self, username, password):
        self.syllabus_pdf = 'timetable.pdf'


    def getPdfFilePath(self) -> str:
        return 'timetable.pdf'

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
    start_end_boxes.map_widget = map_widget
    map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    map_widget.set_address("Toronto")

    map_widget.lower(start_end_boxes)
    # start_end_boxes.days_dropdown.pack()
    root.mainloop()


if __name__ == "__main__":
    main()
