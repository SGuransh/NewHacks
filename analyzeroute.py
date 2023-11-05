from math import sin, cos, sqrt, atan2, radians
import datetime
import csv

example_route = {1: {'coordinates': [(43.6608842, -79.3918635), (43.6599047, -79.3908048), (43.6607327, -79.38568560000002), (43.660575, -79.3856169), (43.660244, -79.38408679999999), (43.6599447, -79.3839571), (43.6597387, -79.3833956), (43.6599137, -79.38262739999999), (43.657374, -79.38144040000002), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ['Head <b>south</b> on <b>Queens Pk Cres W</b> toward <b>Anatomy Ln</b>', 'Slight <b>right</b> toward <b>College St</b>', 'Turn <b>left</b> onto <b>College St</b>', 'Turn <b>right</b> onto <b>Bay St.</b>', 'Turn <b>left</b>', 'Turn <b>right</b> toward <b>Yonge St</b>', 'Turn <b>left</b> toward <b>Yonge St</b>', 'Turn <b>left</b> toward <b>Yonge St</b>', 'Turn <b>right</b> onto <b>Yonge St</b>', 'Turn <b>left</b> onto <b>Gould St</b><div style="font-size:0.9em">Destination will be on the right</div>']}, 2: {'coordinates': [(43.6605903, -79.3912234), (43.65969949999999, -79.3906772), (43.657411, -79.3896742), (43.6589942, -79.38193910000001), (43.6573776, -79.3812349), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ['Head <b>south</b> on <b>Queens Pk Cres W</b> toward <b>Anatomy Ln</b>', 'Continue onto <b>Queens Park</b>', 'Continue onto <b>University Ave</b>', 'Turn <b>left</b> onto <b>Gerrard St W</b>', 'Turn <b>right</b> onto <b>Yonge St</b>', 'Turn <b>left</b> onto <b>Gould St</b><div style="font-size:0.9em">Destination will be on the right</div>']}, 3: {'coordinates': [(43.6643171, -79.3869708), (43.660575, -79.3856169), (43.660244, -79.38408679999999), (43.6599447, -79.3839571), (43.6597387, -79.3833956), (43.6599137, -79.38262739999999), (43.657374, -79.38144040000002), (43.6574131, -79.3810817), (43.6574131, -79.3810817)], 'steps': ['Head <b>east</b> on <b>Wellesley St W</b> toward <b>Queens Pk Cres W</b>', 'Turn <b>right</b> onto <b>Bay St.</b>', 'Turn <b>left</b>', 'Turn <b>right</b> toward <b>Yonge St</b>', 'Turn <b>left</b> toward <b>Yonge St</b>', 'Turn <b>left</b> toward <b>Yonge St</b>', 'Turn <b>right</b> onto <b>Yonge St</b>', 'Turn <b>left</b> onto <b>Gould St</b><div style="font-size:0.9em">Destination will be on the right</div>']}}

class RouteAnalyzer:
    EARTH_RAD = 6373.0
    TIME_WEIGHT = 5
    DISTANCE_WEIGHT = 0.7
    curr_time = datetime.datetime.now()

    def __init__(self, routes: dict, crime_points_file: str):
        self.routes = routes # routes are a list of routes
        self.crime_points = self.getCrimePoints(crime_points_file)
        self.best_route = None

    def getCrimePoints(self, fileName:str) -> dict:
        with open(fileName, newline='', encoding='utf-8') as csv_file:
            # Create a CSV reader
            csv_reader = csv.reader(csv_file)

            # Read the header row
            header = next(csv_reader)

            dic = {}
            for row in csv_reader:
                longe = row[4]
                lat = row[5]
                long_lat = (longe, lat)
                sub_dict = {}
                sub_dict[header[0]] = row[0]
                # sub_dict[header[1]] = row[1]
                sub_dict[header[2]] = row[2]
                sub_dict[header[3]] = row[3]
                dic[long_lat] = sub_dict

            return dic

    # NOTE: points are tuples in the form of (long, lat)
    # Credits: formula from Kurt Peek
    def calcDistanceTwoPoints(self, point1: tuple, point2: tuple) -> float:
        """Returns distance between two points for optim
        parameters:
        - point 1 and point 2 are in the form of (long, lat)

        Credits: formula from Kurt Peek
        """
        R = 6373.0

        lat1 = radians(float(point1[1]))
        lon1 = radians(float(point1[0]))
        lat2 = radians(float(point2[1]))
        lon2 = radians(float(point2[0]))

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return R * c

    def calculateRouteScore(self, route_points: list[tuple]):
        # Note we only check the points in between, not including the destination point because
        # it cannot vary and should therefore not affect the score.

        # process: we want to compare each step point to each crime point. For each point -> compare each point

        total_route_score = 0
        for route_point in route_points:
            point_score = 0
            for crime_point in self.crime_points:
                if self.calcDistanceTwoPoints(crime_point, route_point) <= 0.5:
                    time_score = -1/12 * abs(self.curr_time.hour - self.crime_points[crime_point]["OCC_HOUR"] ) + self.TIME_WEIGHT
                    distance_score = (-1/500 * self.calcDistanceTwoPoints(crime_point, route_point) + 1) * 20
                    point_score += time_score + distance_score + \
                                   self.adjustPremiseType(self.crime_points[crime_point]["PREMISES_TYPE"]) + \
                                   self.adjustMCIType(self.crime_points[crime_point]["MCI_CATEGORY"])

            total_route_score += point_score
        return total_route_score

    def getBestRoute(self) -> dict:
        dic = {}
        best_route = 0
        best_score = 0
        for route in self.routes:
            score = self.calculateRouteScore(self.routes[route]['coordinates'])
            if score < best_score:
                best_score = score
                best_route = route

        dic[best_route] = self.routes[best_route]['coordinates']
        return dic










    def adjustPremiseType(self, premise_type: str) -> float:
        if premise_type == 'Apartment':
            return 10
        elif premise_type == 'Outside':
            return 27
        elif premise_type == 'Transit':
            return 18
        elif premise_type == 'House':
            return 10
        elif premise_type == 'Commercial':
            return 8
        else:
            return 0

    def adjustMCIType(self, premise_type: str) -> float:
        if premise_type == 'Assault':
            return 30
        elif premise_type == 'Robbery':
            return 23
        elif premise_type == 'Auto Theft':
            return 14
        elif premise_type == 'Break and Enter':
            return 20
        elif premise_type == 'Theft Over':
            return 25
        else:
            return 0
