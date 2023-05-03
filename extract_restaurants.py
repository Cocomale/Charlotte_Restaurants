import googlemaps
import pandas as pd

# Enter your Google Maps API key here
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Enter the latitude and longitude of the location you want to search near
location = (35.23159343926886, -80.8419802768916)

# Enter the types of places you want to search for
place_types = ['bar', 'night_club']

# Set a radius for the search, in meters
radius = 2000

# Create an empty list to hold the results
results = []

# Loop over each place type and make a Places API request to search for the places near the location
for place_type in place_types:
    places_result = gmaps.places(query=place_type, location=location, radius=radius)
    
    # Extract the first 20 results
    results += places_result['results']

    # Check if there are more results available
    while 'next_page_token' in places_result:
        # Wait for a few seconds to give the Places API time to generate the next page of results
        import time
        time.sleep(2)
        
        # Make a new request with the pagetoken to retrieve the next page of results
        places_result = gmaps.places(query=place_type, location=location, radius=radius, page_token=places_result['next_page_token'])
        
        # Append the new results to the list of results
        results += places_result['results']

# Create a list of dictionaries containing the name and address of each place
places_list = [{'Place': result['name'], 'Address': result['formatted_address'].split(",")[0], 'Type': place_type} for result in results for place_type in place_types]

# Convert the list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(places_list)

# Group the DataFrame by the name of the place and concatenate all the place types for each name
df_grouped = df.groupby('Place').agg({'Address': 'first', 'Type': lambda x: '/'.join(sorted(set(x))) if len(x) > 1 else x}).reset_index()