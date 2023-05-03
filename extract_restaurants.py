import googlemaps

# Replace YOUR_API_KEY with your actual API key
gmaps = googlemaps.Client(key='AIzaSyDNeWWet_NT8V_nAf0VRJd5wQ5twExm9to')

# Define the location and radius for the search
location = (35.23159343926886, -80.8419802768916)  # Corporate Center, Bank of America
radius = 1000  # 1 km, roughly 0.6 miles

# Define the types of places to search for
place_types = ['bar']

# Make a request to the API
places_result = gmaps.places_nearby(
    location = location,
    radius = radius,
    type = ','.join(place_types)
)

# Iterate through the results and extract the name and address of each place
for place in places_result['results']:
    name = place['name']
    address = place['vicinity']
    print(f'{name}: {address}')