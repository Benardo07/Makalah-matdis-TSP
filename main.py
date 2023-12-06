import googlemaps
import itertools

# Your Google API key
api_key = 'YOUR_API_KEY'

# Initialize the Google Maps client
gmaps = googlemaps.Client(key=api_key)

# List of Mixue locations in Bandung
mixue_locations = [
    "Mixue Cihampelas, Bandung",
    "Mixue Cihampelas Walk (Ciwalk), Bandung",
    "Mixue Surya Sumantri, Bandung",
    "Mixue Cijagra, Bandung",
    # Add the rest of the locations here
]

# Function to calculate distances
def calculate_distances(locations):
    distances = {}
    for loc1, loc2 in itertools.combinations(locations, 2):
        # API call for each pair of locations
        result = gmaps.distance_matrix(origins=[loc1], destinations=[loc2], mode='driving')
        
        # Extract distance
        distance = result['rows'][0]['elements'][0]['distance']['text']
        distances[f"{loc1} to {loc2}"] = distance
    return distances

# Calculate distances
distances = calculate_distances(mixue_locations)

# Print distances
for k, v in distances.items():
    print(f"Distance from {k}: {v}")
