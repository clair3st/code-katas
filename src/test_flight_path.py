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
    assert len(get_data_from_json_url()) == 741


def test_get_data_from_file_returns_list():
    """Test data from json file is in a list."""
    from flight_path import get_data_from_json_file
    assert len(get_data_from_json_file()) == 741