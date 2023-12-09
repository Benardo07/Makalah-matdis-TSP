import requests
import json

def initialize_data():
    """Initializes data for processing."""
    configuration = {
        'google_maps_key': 'AIzaSyCgiERawJtzx3VUILwik5NqftiBCr_wEZY',
        'location_list': [
            '611+Jl+Raya+Terusan+Kopo', '27B+Jl+Tubagus+Ismail', '72F+Jl+Dipati+Ukur', 
            '314A+Jl+Ir+H+Juanda', '160+Jl+Cihampelas', '91+Jl+Ciumbuleuit', 
            '6+Jl+Sukamaju', '15+Jl+Cikondang', '32+Jl+Banda', 
            '41+Jl+Pahlawan', '27B+Jl+Surya+Sumantri', '25A+Jl+Cihapit', '170d+Jl+Setiabudi', 
            '215+Jl+Pasir+Kaliki', '150+Jl+Cikutra', 'Istana+BEC', 
            'Mixue+Dago+Atas', '30+Jl+Kebon+Kawung', '122B+Jl+Pajajaran', 
             '125+Jl+Cibadak'
        ]
    }
    return configuration

def generate_distance_matrix(data):
    """Generates a distance matrix from the provided data."""
    locations = data['location_list']
    api_key = data['google_maps_key']
    max_elements_per_request = 100
    total_locations = len(locations)
    max_rows_per_request = max_elements_per_request // total_locations
    num_full_requests, remainder = divmod(total_locations, max_rows_per_request)
    matrix = []

    for i in range(num_full_requests):
        start_index = i * max_rows_per_request
        end_index = start_index + max_rows_per_request
        origins = locations[start_index:end_index]
        matrix.extend(process_request(origins, locations, api_key))

    if remainder:
        origins = locations[-remainder:]
        matrix.extend(process_request(origins, locations, api_key))

    return matrix

def process_request(origins, destinations, key):
    """Processes a single request to the Distance Matrix API."""
    def construct_query(locations):
        return '|'.join(locations)

    base_url = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial'
    query = f"{base_url}&origins={construct_query(origins)}&destinations={construct_query(destinations)}&key={key}"
    response = json.loads(requests.get(query).text)
    return parse_response(response)

def parse_response(api_response):
    """Parses the response from the API into a usable format."""
    matrix_section = []
    for row in api_response['rows']:
        distances = [element.get('distance', {}).get('value', 'N/A') for element in row['elements']]
        matrix_section.append(distances)
    return matrix_section

# Main execution
configuration = initialize_data()
distance_matrix_result = generate_distance_matrix(configuration)
print(distance_matrix_result)
