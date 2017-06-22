"""Test implementation of a simple unweighted directed graph."""

import pytest


@pytest.fixture
def sample_graph():
    """Create testing graph."""
    from src.weighted_graph import Graph
    one_graph = Graph('A')
    empty_graph = Graph()
    new_graph = Graph(['A', 'B', 'C', 'D'])
    return one_graph, empty_graph, new_graph


def test_initialization_of_graph(sample_graph):
    """Test initilaization of an empty graph."""
    assert sample_graph[1].graph == {}


def test_initialization_of_graph_with_one_datapoint(sample_graph):
    """Test initialization of a graph with one data point."""
    assert sample_graph[0].graph == {'A': []}


def test_initialization_of_graph_with_multiple_datapoints(sample_graph):
    """Test graph with multiple data points is initialized."""
    assert sample_graph[2].graph == {'A': [], 'B': [], 'C': [], 'D': []}


def test_add_a_node_adds_node_with_no_connections(sample_graph):
    """Test add_node adds a node to graph with no connections."""
    sample_graph[1].add_node('B')
    assert sample_graph[1].graph == {'B': []}


def test_add_a_node_to_an_initialized_graph(sample_graph):
    """Test node is added to an existing graph."""
    sample_graph[2].add_node('E')
    assert sample_graph[2].graph == {'A': [], 'B': [], 'C': [],
                                     'D': [], 'E': []}


def test_add_existing_node_do_not_duplicate(sample_graph):
    """Test add and existingnode does not duplicate in graph."""
    sample_graph[0].add_node('A')
    assert sample_graph[0].graph == {'A': []}


def test_add_edge_on_existing_nodes(sample_graph):
    """Test connections between existing nodes is created."""
    sample_graph[2].add_edge('A', 'B')
    assert sample_graph[2].graph['A'] == [('B', 1)]


def test_add_edge_when_node2_does_not_exist(sample_graph):
    """Test connection between new node2 and existing is made."""
    sample_graph[0].add_edge('A', 'B')
    assert sample_graph[0].graph == {'A': [('B', 1)], 'B': []}


def test_add_edge_when_node1_does_not_exist(sample_graph):
    """Test connection between new node1 and existing node2."""
    sample_graph[0].add_edge('B', 'A')
    assert sample_graph[0].graph == {'A': [], 'B': [('A', 1)]}


def test_add_edge_when_node1_and_node2_does_not_exist(sample_graph):
    """Test connection between new node1 and new node2."""
    sample_graph[1].add_edge('A', 'B')
    assert sample_graph[1].graph == {'A': [('B', 1)], 'B': []}


def test_list_of_nodes_is_displayed(sample_graph):
    """Test nodes are displayed in a list."""
    assert sample_graph[0].nodes() == ['A']
    assert sample_graph[1].nodes() == []


def test_list_of_multiple_nodes_is_displayed(sample_graph):
    """Test nodes in a graph of multiple nodes are returned."""
    many_nodes = sample_graph[2].nodes()
    many_nodes.sort()
    assert many_nodes == ['A', 'B', 'C', 'D']


def test_edges_are_displayed(sample_graph):
    """Test all edges are displayed in a list."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('C', 'A')
    sample_graph[2].add_edge('C', 'B')
    all_edges = sample_graph[2].edges()
    assert sorted(all_edges) == [('A', 'B', 1), ('C', 'A', 1), ('C', 'B', 1)]


def test_edges_when_there_are_none(sample_graph):
    """Test no edges are displayed when there are none."""
    assert sample_graph[2].edges() == []


def test_delete_invalid_node(sample_graph):
    """Test deletion of node when it does not exist."""
    with pytest.raises(IndexError):
        assert sample_graph[2].del_node('X')


def test_delete_from_empty_graph(sample_graph):
    """Test deletion from src.empty graph."""
    with pytest.raises(IndexError):
        assert sample_graph[0].del_node('X')


def test_delete_node_from_sample_graph(sample_graph):
    """Test deletion from src.sample graph."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    sample_graph[2].add_edge('A', 'D')
    sample_graph[2].del_node('B')
    assert 'B' not in sample_graph[2].graph


def test_del_node_from_graph_removed_edge(sample_graph):
    """Test deleted node is removed from src.edges."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    sample_graph[2].add_edge('A', 'D')
    sample_graph[2].del_node('B')
    assert 'B' not in sample_graph[2].graph['A']


def test_delete_edge(sample_graph):
    """Test deletion of edge from src.graph."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    sample_graph[2].add_edge('A', 'D')
    sample_graph[2].del_edge('A', 'B')
    assert sample_graph[2].graph['A'] == [('C', 1), ('D', 1)]


def test_delete_invalid_edge(sample_graph):
    """Test deletion of invalid edge from src.graph."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    sample_graph[2].add_edge('A', 'D')
    with pytest.raises(IndexError):
        assert sample_graph[2].del_edge('A', 'X')


def test_had_valid_node(sample_graph):
    """Test that has_node works correctly for valid node."""
    assert sample_graph[2].has_node('A')


def test_had_invalid_node(sample_graph):
    """Test that has_node works correctly for invalid node."""
    assert not sample_graph[2].has_node('X')


def test_neighbors_invalid(sample_graph):
    """Test that neighbors throws error if invalid node."""
    with pytest.raises(KeyError):
        assert sample_graph[2].neighbours('X')


def test_neighbors_invalid_empty(sample_graph):
    """Test that neighbors throws error on empty graph."""
    with pytest.raises(KeyError):
        assert sample_graph[0].neighbours('X')


def test_neighbors_valid(sample_graph):
    """Test that neighbors returns node connections."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    sample_graph[2].add_edge('A', 'D')
    assert sample_graph[2].neighbours('A') == ['B', 'C', 'D']


def test_adjacent_invalid(sample_graph):
    """Test that adjacent throws error if invalid node."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    sample_graph[2].add_edge('A', 'D')
    with pytest.raises(KeyError):
        assert sample_graph[2].adjacent('X', 'A')
    with pytest.raises(KeyError):
        assert sample_graph[2].adjacent('B', 'X')


def test_adjacent_for_invalid_edge(sample_graph):
    """Test that adjacent returns False if edge does not exist."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    assert not sample_graph[2].adjacent('A', 'D')


def test_adjacent_for_valid_edge(sample_graph):
    """Test that adjacent returns True for existing edgge."""
    sample_graph[2].add_edge('A', 'B')
    sample_graph[2].add_edge('A', 'C')
    assert sample_graph[2].adjacent('A', 'C')


def test_edges_have_default_weight_of_one(sample_graph):
    """Test added edges have a default weight of 1."""
    sample_graph[2].add_edge('A', 'B')
    assert sample_graph[2].graph['A'][0][1] == 1


def test_edges_have_weight_other_than_one(sample_graph):
    """Test added edges have a specified weight."""
    sample_graph[2].add_edge('A', 'B', 2)
    assert sample_graph[2].graph['A'][0][1] == 2


def test_weight_can_only_be_a_number(sample_graph):
    """Test weight can only be a number."""
    with pytest.raises(ValueError):
        sample_graph[2].add_edge('A', 'B', 'C')
