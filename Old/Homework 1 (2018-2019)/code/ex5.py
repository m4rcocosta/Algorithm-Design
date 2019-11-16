class Graph(object):
    def __init__(self, t="undirected"):
        self.vertex = []
        self.edges = []
        self.t = t

    def get_nodes(self):
        return self.vertex

    def get_edges(self):
        return self.edges

    def get_out_edges(self, node):
        edges = []
        for e in self.get_edges():
            if e[0] == node and e not in edges:
                    edges.append(e)
            if self.t == "undirected" and e[1] == node and e not in edges:
                    edges.append(e)

        return edges

    def add_node(self, node):
        if node not in self.vertex:
            self.vertex.append(node)

    def add_edge(self, edge):
        if edge not in self.edges:
            self.edges.append(edge)

    def sorted_by_weight(self, desc=False):
        return sorted(self.get_edges(), key=lambda x: x[2], reverse=desc)

    def get_min_edges(self, node, weight):
        neighbours = self.get_out_edges(node)
        min_edges = set()
        for edge in neighbours:
            if edge[2] < weight:
                min_edges.add(edge)
        return min_edges

    def edge_in_mst_aux(self, edge, dest, weight, visited=None):
        if visited is None:
            visited = set()
        node = edge[1]
        if node in visited:
            return True
        visited.add(node)
        if len(self.get_out_edges(node)) == 0:
            return True
        node_min_edges = self.get_min_edges(node, weight)
        if len(node_min_edges) == 0:
            return True
        for next in node_min_edges:
            n2 = next[1]
            if n2 in visited:
                continue
            if n2 == dest:
                return False
            elif n2 not in visited:
               return self.edge_in_mst_aux(next, dest, weight, visited)
        return True

    def edge_in_mst(self, edge):
        return self.edge_in_mst_aux(edge, edge[0], edge[2])


    def kruskal(self):
        parent = dict()
        rank = dict()

        for vertex in self.vertex:
            parent[vertex] = vertex
            rank[vertex] = 0

        def find(vertex):
            if parent[vertex] != vertex:
                parent[vertex] = find(parent[vertex])
            return parent[vertex]

        def union(vertex1, vertex2):
            root1 = find(vertex1)
            root2 = find(vertex2)
            if rank[root1] < rank[root2]:
                parent[root1] = root2
            elif rank[root1] > rank[root2]:
                parent[root2] = root1
            else:
                parent[root2] = root1
                rank[root2] += 1

        mst = Graph("directed")
        minimum_spanning_tree = set()
        edges = self.sorted_by_weight()
        for edge in edges:
            v1, v2, w = edge
            if find(v1) != find(v2):
                union(v1, v2)
                minimum_spanning_tree.add(edge)
        for node in self.get_nodes():
            mst.add_node(node)
        for edge in minimum_spanning_tree:
            mst.add_edge(edge)
        return mst

    def give_a_mst(self, edge):
        if self.edge_in_mst(edge):
            print("The edge",str(edge),"belongs to MST!")
            print("Minimum Spanning Tree:", end="")
            return self.kruskal()
        else:
            print("The edge",str(edge),"doesn't belong to MST!")
            return None

    def __len__(self):
        return len(self.vertex)

    def __str__(self):
        result = "\n"
        nodes = self.vertex
        nodes.sort()
        for node in nodes:
            result += node+": "
            neighbours = self.get_out_edges(node)
            neig = []
            for n in neighbours:
                if n[0] == node:
                    neig.append((n[1], n[2]))
                else:
                    neig.append((n[0], n[2]))
            neig.sort()
            for n in neig:
                result += n[0]+"("+str(n[1])+") "
            result += "\n"
        return result

graph = Graph("undirected")
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")
graph.add_node("F")
graph.add_edge(('A', 'B', 5))
graph.add_edge(('A', 'F', 8))
graph.add_edge(('B', 'C', 3))
graph.add_edge(('B', 'F', 9))
graph.add_edge(('C', 'D', 18))
graph.add_edge(('C', 'A', 4))
graph.add_edge(('D', 'F', 7))
graph.add_edge(('D', 'E', 2))
graph.add_edge(('E', 'F', 2))
graph.add_edge(('F', 'C', 6))

print("Graph:", end="")
print(graph)
print("="*50)
print("Minimum Spanning Tree:", end="")
print(graph.kruskal())

test_edge = ('A', 'F', 8)
print("="*50)
print("Testing if the edge",str(test_edge),"belongs to the MST!\n")
print(graph.give_a_mst(test_edge))

test_edge = ('E', 'F', 2)
print("="*50)
print("Testing if the edge",str(test_edge),"belongs to the MST!\n")
print(graph.give_a_mst(test_edge))