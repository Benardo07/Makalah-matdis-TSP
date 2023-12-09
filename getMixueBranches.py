import googlemaps
import pandas as pd
import time

def fetch_places(query, gmaps_client):
    places = []
    search_result = gmaps_client.places(query=query, type='establishment', region='.id')

    # Paginate through results
    while True:
        places.extend(search_result.get('results', []))
        page_token = search_result.get('next_page_token')

        if not page_token:
            break

        time.sleep(2)  # Necessary to wait for the token to become valid
        search_result = gmaps_client.places(query=query, type='establishment', region='.id', page_token=page_token)

    return places

# Set up the Google Maps client
gmaps = googlemaps.Client(key='AIzaSyCgiERawJtzx3VUILwik5NqftiBCr_wEZY')

# Search for Mixue branches in Bandung
mixue_branches = fetch_places('Mixue Bandung', gmaps)

# Process and store data in a table
data = []
for place in mixue_branches:
    # Get detailed information
    details = gmaps.place(place_id=place['place_id'])['result']

    address = details.get('formatted_address', '')
   
    data.append({
        'Name': place.get('name', ''),
        'Address': address
    })

# Convert to DataFrame
df = pd.DataFrame(data)
print(df)

# Save to CSV
df.to_csv('mixue_branches.csv', index=False)
