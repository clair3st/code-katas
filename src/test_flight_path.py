"""Test flight path route calculator."""

import pytest


@pytest.fixture()
def flight_graph():
    """Fixture for graph."""
    from flight_path import make_airport_graph, parse_data_into_required_format, get_data_from_json_file
    graph = make_airport_graph(
        parse_data_into_required_format(
            get_data_from_json_file()
        ))
    return graph


def test_get_data_from_url_returns_list():
    """Test data from json url is in a list with length."""
    from flight_path import get_data_from_json_url
    data = get_data_from_json_url()
    assert len(data) == 741


def test_get_data_from_file_returns_list():
    """Test data from json file is in a list."""
    from flight_path import get_data_from_json_file
    assert len(get_data_from_json_file()) == 741


def test_parse_data_into_required_format():
    """Test data is parsed into correct format."""
    from flight_path import parse_data_into_required_format
    data = [
        {"city": "Goma",
         "connection_urls": [
             "https://en.wikipedia.org/wiki/Kindu_Airport",
             "https://en.wikipedia.org/wiki/Bangoka_International_Airport",
             "https://en.wikipedia.org/wiki/N%27djili_Airport",
             "https://en.wikipedia.org/wiki/Addis_Ababa_Bole_International_Airport"
         ],
         "url": "https://en.wikipedia.org/wiki/Goma_International_Airport",
         "country": "Democratic Republic of the Congo",
         "destination_cities": ["Kinshasa", "Kisangani", "Addis Ababa"],
         "destination_airports": [
             "N'djili Airport",
             "Bangoka International Airport",
             "Addis Ababa Bole International Airport"],
         "airport": "Goma International Airport",
         "lat_lon": [-1.669889, 29.238278]}
    ]

    parse_data = parse_data_into_required_format(data)
    expected = {'Goma': {
                'lat_lon': [-1.669889, 29.238278],
                'connections': ['Kinshasa', 'Kisangani', 'Addis Ababa']}}
    assert parse_data == expected


def test_flight_path_shortest_path_no_connections(flight_graph):
    """Test a known flight path returns the correct distance."""
    from flight_path import return_shortest_route

    trip = return_shortest_route(flight_graph, 'Sydney', 'London')

    assert trip == (10536.109189807654, ['Sydney', 'London'])


def test_flight_path_shortest_path_connections(flight_graph):
    """Test a known flight path returns the correct conncetions."""
    from flight_path import return_shortest_route

    trip = return_shortest_route(flight_graph, 'Sydney', 'Goma')

    assert trip[1] == ['Sydney', 'Perth', 'Plaine Magnien', 'Dar es Salaam', 'Addis Ababa', 'Goma']


def test_flight_path_shortest_path_no_result(flight_graph):
    """Test an unknown route raises an error."""
    from flight_path import return_shortest_route

    with pytest.raises(KeyError):
        return_shortest_route(flight_graph, 'Sydney', 'Canberra')
