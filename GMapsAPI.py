import googlemaps
from datetime import datetime


class GMapsAPI:
    SAMPLE_ROUTE_FORMAT = {1: {'coordinates': [(43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ['Walk to 335 Yonge St, Toronto, ON M5B 2L3, Canada']}, 2: {'coordinates': [(43.659248, -79.390289), (43.6562811, -79.380459), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ["Walk to Queen's Park", 'Subway towards Yonge-University to Finch Station', 'Walk to 335 Yonge St, Toronto, ON M5B 2L3, Canada']}, 3: {'coordinates': [(43.6596826, -79.3907918), (43.6614659, -79.3828636), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ["Walk to College St at University Ave - Queen's Park Station", 'Streetcar towards Carlton to Main Street Station', 'Walk to 335 Yonge St, Toronto, ON M5B 2L3, Canada']}, 4: {'coordinates': [(43.659248, -79.390289), (43.6562811, -79.380459), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ["Walk to Queen's Park", 'Subway towards Yonge-University to Finch Station', 'Walk to 335 Yonge St, Toronto, ON M5B 2L3, Canada']}, 5: {'coordinates': [(43.6639524, -79.3871578), (43.657212, -79.3845424), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ['Walk to Bay St at Wellesley St West South Side', 'Bus towards Bay to Queens Quay and Sherbourne', 'Walk to 335 Yonge St, Toronto, ON M5B 2L3, Canada']}, 6: {'coordinates': [(43.6596826, -79.3907918), (43.6614659, -79.3828636), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ["Walk to College St at University Ave - Queen's Park Station", 'Streetcar towards Carlton to Main Street Station', 'Walk to 335 Yonge St, Toronto, ON M5B 2L3, Canada']}}
    SAMPLE_CRIME_HEAVY = {1: {'coordinates': [(43.6585663, -79.39721589999999), (43.659308, -79.397475), (43.6600245, -79.3970369), (43.6600684, -79.396902), (43.66452169999999, -79.3987034), (43.66452169999999, -79.3987034)], 'steps': ['Head <b>east</b> on <b>College St</b>', 'Turn <b>left</b><div style="font-size:0.9em">Take the stairs</div>', 'Walk for 110m', 'Head <b>northeast</b> toward <b>St George St</b>', 'Turn <b>left</b> onto <b>St George St</b><div style="font-size:0.9em">Destination will be on the right</div>']}, 2: {'coordinates': [(43.6587964, -79.39596569999999), (43.66452169999999, -79.3987034), (43.66452169999999, -79.3987034)], 'steps': ['Head <b>east</b> on <b>College St</b> toward <b>Ross St</b>', 'Sharp <b>left</b> onto <b>St George St</b><div style="font-size:0.9em">Destination will be on the right</div>']}, 3: {'coordinates': [(43.6583516, -79.3983101), (43.6600712, -79.3989983), (43.6601575, -79.39864209999999), (43.6631998, -79.3998648), (43.6632239, -79.3997809), (43.6635859, -79.39915429999999), (43.6636271, -79.3991293), (43.6639272, -79.3985749), (43.66452169999999, -79.3987034), (43.66452169999999, -79.3987034)], 'steps': ['Head <b>west</b> on <b>College St</b> toward <b>Huron St</b>', 'Turn <b>right</b> onto <b>Huron St</b>', 'Turn <b>right</b> onto <b>Ursula Franklin St</b>', 'Turn <b>left</b> onto <b>Huron St</b>', 'Turn <b>right</b> toward <b>Harbord St</b>', 'Slight <b>left</b> toward <b>Harbord St</b>', 'Turn <b>left</b> toward <b>Harbord St</b>', 'Turn <b>right</b> onto <b>Harbord St</b>', 'Turn <b>left</b> onto <b>St George St</b><div style="font-size:0.9em">Destination will be on the right</div>']}}
    def __int__(self):
        pass

    def getRoutes(self, origin: any, destination: any, travel_mode: str):
        """
        Parameters:
        -origin/destination: this has been tested on inputs with origin and destination as a string representing
        longitude and latitude as follows:
            origin = "41.03, 56.00"
        -travel_mode: can be "driving", "walking", "bicycling", "transit"
        """
        print('danger:made api call')
        gmaps = googlemaps.Client(key='AIzaSyAtO23OblmhtyzSFk9Kah5FSbPUd-9FQQk')

        # Request multiple routes with alternative routes
        routes = gmaps.directions(
            origin,
            destination,
            mode=travel_mode,
            departure_time=datetime.now(),
            alternatives=True  # Request multiple routes
        )

        return routes

    def getRoutesFormattedSample(self):
        return self.SAMPLE_ROUTE_FORMAT

    def formatRoutes(self, routes):
        route_info = dict()
        index = 1
        for i in routes:
            coordinates_for_this_route = []
            html_steps = []

            for j in i["legs"][0]["steps"]:
                coordinates_for_this_route.append(
                    (j["end_location"]["lat"], j["end_location"]["lng"]))
                html_steps.append(j["html_instructions"])
            coordinates_for_this_route.append(
                (i["legs"][0]["end_location"]["lat"], i["legs"][0]["end_location"]["lng"]))
            route_info[index] = {"coordinates": coordinates_for_this_route, "steps": html_steps}
            index += 1

        print(route_info)
        return route_info

    def getStepCoords(self, formatted_routes: dict):
        return formatted_routes["coordinates"]
