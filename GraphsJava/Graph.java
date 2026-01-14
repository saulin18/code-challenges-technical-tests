
//Description:
//In this Kata, you will be given a graph consisting of Vertices and Edges, and your task is to complete the following function:
//
//public static Set<Vertex> getNeighbours(Graph graph, Vertex vertex)
//
//This function will receive the graph and a vertex as a parameter, and should return all neighbours of the vertex in the graph. No vertex is a neighbour of itself.
//
//This is a traditional, undirected, unweighted - however not necessarily connected - graph without duplicate vertices. The graph consists of Vertex and Edge objects: each edge will have 2 different vertex endpoints, but not all vertices may be on vertices.
//
//Graph, Vertex and Edge will all be preloaded for you and should not be modified. However, for simpler offline development and better understanding the full code of these classes will be provided in the end of the description. The methods that should interest you in this Kata are the following:
//
// public Set<Vertex> getVertices() in Graph that returns a set of all vertices of the graph.
//
//public Set<Edge> getEdges() in Graph that returns a set of all vertices of the graph.
//
//public Vertex getV1() and public Vertex getV2() in Edge that return the Vertex endpoints of an edge.
//
//Both Vertex and Edge has hashCode and equals implemented.
//
//Please note the following:
//
//Though Vertex objects store no value, a unique identifier is generated for them so hashcode and equals can be used
//Two vertices are considered equal if they contain the same nodes regardless of the order of nodes - remember, this is an undirected graph
//The vertex parameter will always be a vertex of the graph
//Happy coding! Don't forget to rate this Kata and don't hesitate to leave feedback in the comments!
import java.util.*;

public class Graph {

    private static int uidCounter = 0;
    Set<Vertex> vertices;


    public Graph() {
        vertices = new HashSet<>();
        vertices = new HashSet<>();
    }

    public void addVertex(Vertex vertex) {
        vertices.add(vertex);
    }

    public void addVertices(Vertex... vertices) {
        for (Vertex v : vertices) {
            addVertex(v);
        }
    }

    public void addEdge(Vertex v1, Vertex v2) {
        addEdge(new Edge(v1, v2));
    }

    public void addEdge(Edge edge) {
        vertices.add(edge.v1);
        vertices.add(edge.v2);
        vertices.add(edge);
    }

    public void addEdges(Vertex... vertices) {
        if (vertices.length % 2 != 0) {
            throw new IllegalArgumentException();
        }

        for (int i = 0; i < vertices.length; i = i + 2) {
            addEdge(vertices[i], vertices[i + 1]);
        }
    }

    public Set<Vertex> getVertices() {
        return vertices;
    }

    public Set<Edge> getEdges() {
        return vertices;
    }

    static int getUidForNode() {
        return uidCounter++;
    }

    public static Set<Vertex> getNeighbours(Graph graph, Vertex vertex) {
        Set<Vertex> neighbours = new HashSet<>();

        for (Edge edge : graph.getEdges()) {
            Vertex v1 = edge.getV1();
            Vertex v2 = edge.getV2();

            if (v1.equals(vertex)) {
                neighbours.add(v2);
            } else if (v2.equals(vertex)) {
                neighbours.add(v1);
            }
        }
        return neighbours;
    }

    public static int hopDistance(Graph graph, Vertex source, Vertex target) {

        if (!graph.getVertices().contains(source)
                || !graph.getVertices().contains(target)) {
            return -1;
        }

        if (source.equals(target)) {
            return 0;
        }

        var queue = new LinkedList<Vertex>();
        var map = new HashMap<>();
        var seen = new HashSet<Vertex>();
        queue.add(source);
        seen.add(source);
        map.put(source, 0);

        while (!queue.isEmpty()) {
            var element = queue.poll();
            int currentDistance = (int) map.get(element);

            if (element.equals(target)) {
                return currentDistance;
            }

            var neighbours = graph.getNeighbours(graph, element);

            for (Vertex neighbour : neighbours) {
                if (!seen.contains(neighbour)) {
                    seen.add(neighbour);
                    map.put(neighbour, currentDistance + 1);
                    queue.add(neighbour);

                }

            }

        }

        return -1;
    }

    public static int departmentConnections(Graph graph, Set<Vertex> department1, Set<Vertex> department2) {
    

        var vertices = graph.getEdges();
        int res = 0;
        for (Edge edge : vertices) {
            var left = edge.v1;
            var right = edge.v2;

            if ((department1.contains(left) && department2.contains(right))
                    || (department1.contains(right) && department2.contains(left))) {
                res += 1;
            }

        }

        return res;
    }

    public static boolean isConnected(Graph graph) {
        var vertices = graph.getVertices();

        if (vertices.size() < 1)
            return true;

        var visited = new HashSet<Vertex>();
        var queue = new LinkedList<Vertex>();
        var firstElement = vertices.iterator().next();
        visited.add(firstElement);
        queue.add(firstElement);

        var element = queue.poll();
        DFS(element, graph, visited);
        if (visited.containsAll(vertices))
            return true;
        return false;

    }

    public static void DFS(Vertex current, Graph graph, Set<Vertex> visited) {
        visited.add(current);

        Set<Vertex> neighbours = getNeighbours(graph, current);
        for (Vertex neighbour : neighbours) {
            if (!visited.contains(neighbour)) {
                DFS(neighbour, graph, visited); // Recursión
            }
        }
    }

    public void BFS(Vertex start, Graph graph){
        Set<Vertex> visited = new HashSet<>();
        Queue<Vertex> queue = new LinkedList<>();

        visited.add(start);
        queue.add(start);

        while (!queue.isEmpty()) {
            
            var current  = queue.poll();
    
            if (!visited.contains(current)) {
                visited.add(current);
                for (Vertex vertex : Graph.getNeighbours(graph, current)) {
                    if (!visited.contains(vertex)) {
                         queue.add(vertex);
                         visited.add(vertex);
                    }
                   
                }
            }
        }
        return;
    }
}
