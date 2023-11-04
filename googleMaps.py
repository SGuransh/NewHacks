import googlemaps
from datetime import datetime

# Replace 'YOUR_API_KEY' with your actual API key
gmaps = googlemaps.Client(key='AIzaSyAtO23OblmhtyzSFk9Kah5FSbPUd-9FQQk')

# Define the origin and destination
origin = "43.662891, -79.393337"
destination = "43.657312, -79.381037"

# Set the mode of travel (e.g., "driving," "walking," "transit")
travel_mode = "transit"

# Request multiple routes with alternative routes
routes = gmaps.directions(
    origin,
    destination,
    mode=travel_mode,
    departure_time=datetime.now(),
    alternatives=True  # Request multiple routes
)

# Loop through the routes and print information
for i, route in enumerate(routes):
    print(f"Route {i + 1} - Distance: {route['legs'][0]['distance']['text']}, Duration: {route['legs'][0]['duration']['text']}")

print(routes)

# first_route = routes[0]
# for step in first_route['legs'][0]['steps']:
#     print(step['html_instructions'])
