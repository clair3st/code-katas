"""Implementation of a simple graph in Python."""


class Graph(object):
    """Implementation of a simple directed Graph.

    g.nodes(): return a list of all nodes in the graph.

    g.edges(): return a list of all edges in the graph.

    g.add_node(n): adds a new node n to the graph.

    g.add_edge(n1, n2, weight): adds a new edge to the graph connecting n1 n2,
     if either n1 or n2 are not already present in the graph,
     they should be added.

    g.del_node(n): deletes the node n from the graph, raises an error
     if no such node exists

    g.del_edge(n1, n2): deletes the edge connecting n1 and n2 from the
     graph, raises an error if no such edge exists

    g.has_node(n): True if node n is contained in the graph,
     False if not.

    g.neighbors(n): returns the list of all nodes connected to n by
     edges, raises an error if n is not in g

    g.adjacent(n1, n2): returns True if there is an edge connecting n1
     and n2, False if not, raises an error if either of the supplied nodes
     are not in g

    g.depth_first_traversal(start): Perform a full depth-first traversal of
    the graph beginning at start. Return the full visited path when traversal
    is complete.

    g.breadth_first_traversal(start): Perform a full breadth-first traversal
    of the graph, beginning at start. Return the full visited path when
    traversal is complete.



    References:
    https://www.python.org/doc/essays/graphs/
    https://medium.freecodecamp.com/a-gentle-introduction-to-data-structures-how-graphs-work-a223d9ef8837#.6xbpr1l6q
    http://stackoverflow.com/questions/19472530/representing-graphs-data-structure-in-python
    """

    def __init__(self, data=None):
        """Initialize a graph instance.

        Data is the key of the dict and edges are held in a list of names.
        """
        self.graph = {}
        if data:
            for i in data:
                self.add_node(i)

    def nodes(self):
        """Return a list of all nodes in graph."""
        return [key for key in self.graph.keys()]

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        if self.nodes:
            for node1 in self.graph:
                for node2 in self.graph[node1]:
                    edge_list.append((node1, node2[0], node2[1]))
        return edge_list

    def add_node(self, node):
        """Add a new node to graph."""
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2, weight=1):
        """Add an edge between node1 and node2."""
        self.graph.setdefault(node1, [])
        self.graph.setdefault(node2, [])
        if node2 not in self.graph[node1]:
            self.graph[node1].append((node2, weight))

    def del_node(self, node_delete):
        """Delete the inputted node from the graph."""
        if node_delete not in self.graph:
            raise IndexError('The input node is not in the graph')
        del self.graph[node_delete]
        for node in self.graph:
            for edge in self.graph[node]:
                if edge[0] == node_delete:
                    self.graph[node].remove(edge)

    def del_edge(self, node1, node2):
        """Delete the edge connecting node1 to node 2 if it exists."""
        if node2 not in [edge[0] for edge in self.graph[node1]]:
            raise IndexError('This edge does not exist.')

        removed_edge = [edge for edge in self.graph[node1] if edge[0] == node2]
        self.graph[node1].remove(removed_edge[0])

    def has_node(self, node):
        """Return true if the input node is in the graph, else False."""
        return node in self.graph

    def neighbours(self, node):
        """Return the list of nodes connected to the input node."""
        return [edge[0] for edge in self.graph[node]]

    def adjacent(self, node1, node2):
        """Return True if there is an edge connecting n1 and n2."""
        if node1 not in self.graph or node2 not in self.graph:
            raise KeyError('One or both of these nodes is not in the graph.')
        return node2 in [edge[0] for edge in self.graph[node1]]

    def depth_traversal(self, root, visited=None):
        """Perform depth traversal of graph."""
        if visited is None:
            visited = []
        visited.append(root)
        for edge in self.graph[root]:
            if edge[0] not in visited:
                self.depth_traversal(edge[0], visited)
        return visited

    def breadth_traversal(self, root):
        """Perform breath traversal of graph."""
        visited = [root]
        node_edges = self.graph[root]
        while node_edges:
            edge = node_edges.pop(0)
            if edge[0] not in visited:
                visited.append(edge[0])
                unique_edges = [edge[0] for edge in self.graph[edge]
                                if edge[0] not in visited]
                node_edges.extend(unique_edges)
        return visited

    def dijkstra(self, source, target):
        """Find the shorted path from source node to all other nodes."""
        visited = {source: 0}
        path = {}
        nodes_visit = self.nodes()
        while nodes_visit:
            min_node = None
            for node in nodes_visit:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node
            if min_node is None:
                break

            nodes_visit.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.graph[min_node]:
                weight = current_weight + edge[1]
                if edge[0] not in visited or weight < visited[edge[0]]:
                    visited[edge[0]] = weight
                    path[edge[0]] = min_node

            if min_node == target:
                # a = [c for c, v in path.items()]
                # a.sort()
                # print(a)
                # print(min_node, target)
                # print(visited)
                return visited[target], self._path(source, target, path)

    def _path(self, source, target, path):
        """Helper function to return a list of the path."""
        cur_node = target
        ret_path = [target]
        while cur_node != source:
            ret_path.append(path[cur_node])
            cur_node = path[cur_node]
        return ret_path[::-1]


if __name__ == '__main__':
    import timeit
    graph = Graph(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('A', 'E')
    graph.add_edge('B', 'D')
    graph.add_edge('B', 'F')
    graph.add_edge('C', 'G')
    graph.add_edge('E', 'F')
    print('Depth Traversal Time for 1000 traversals:',
          timeit.timeit(stmt="graph.depth_traversal('A')",
                        setup='from __main__ import graph',
                        number=1000))
    print('Breadth Traversal Time for 1000 traversals:',
          timeit.timeit(stmt="graph.breadth_traversal('A')",
                        setup='from __main__ import graph',
                        number=1000))
