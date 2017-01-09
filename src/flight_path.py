"""Find the distance between two cities."""
import requests
from weighted_graph import Graph
import sys
import json


def calculate_distance(point1, point2):
    """Calculate the distance (in miles) between point1 and point2.

    point1 and point2 must have the format [latitude, longitude].
    The return value is a float.

    Modified and converted to Python from:
    http://www.movable-type.co.uk/scripts/latlong.html
    """
    import math

    def convert_to_radians(degrees):
        return degrees * math.pi / 180

    radius_earth = 6.371E3  # km
    phi1 = convert_to_radians(point1[0])
    phi2 = convert_to_radians(point2[0])
    delta_phi = convert_to_radians(point1[0] - point2[0])
    delta_lam = convert_to_radians(point1[1] - point2[1])

    a = math.sin(0.5 * delta_phi)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(0.5 * delta_lam)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return radius_earth * c / 1.60934  # convert km to miles


def get_data_from_json_url():
    """Extract information from json url."""
    url = 'https://codefellows.github.io/sea-python-401d5/_downloads/cities_with_airports.json'
    response = requests.get(url)
    return response.json()


def get_data_from_json_file():
    """Extract information from json file."""
    with open('cities_with_airports.json') as data_as_json:
            data = json.load(data_as_json)
    return data


def parse_data_into_required_format(data):
    """Take data of airports and format into dictionary."""
    airport_data = {airport['city']: {
        'connections': airport['destination_cities'],
        'lat_lon': airport['lat_lon']
    } for airport in data}

    return airport_data


def make_airport_graph(airport_data):
    """Using the airport information make a simple weighted graph."""
    world_map = Graph()

    for city in airport_data:
        for destination in airport_data[city]['connections']:
            try:
                world_map.add_edge(
                    city,
                    destination,
                    calculate_distance(airport_data[city]['lat_lon'],
                                       airport_data[destination]['lat_lon'])
                )
            except KeyError:
                continue

    return world_map


def return_shortest_route(graph, start, destination):
    """Return the shortest routes between two cities."""
    result = graph.dijkstra(start, destination)
    if result is None:
        raise KeyError('No such journey possible')
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        graph = make_airport_graph(
            parse_data_into_required_format(
                get_data_from_json_file()
            )
        )
    else:
        graph = make_airport_graph(
            parse_data_into_required_format(
                get_data_from_json_url()
            )
        )

    print(return_shortest_route(graph, 'Sydney', 'London'))
    print(return_shortest_route(graph, 'Sydney', 'Canberra'))
