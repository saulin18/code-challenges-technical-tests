import java.util.*;
final class Node {
    String value;
    List<Node> edges = new ArrayList<>();
    
    public Node(String value) {
      this.value = value;
    }
          
    public Node(String value, List<Node> edges) {
      this.value = value;
      this.edges = edges;
    }
  }



public class CheckPath {
    public static boolean getRoute(Node a, Node b) {

      if(a == b) return false;
      
      var visited = new HashSet<Node>();

      DFS(a, visited);

      return visited.contains(b);
    }

    //In the path we will add all nodes we visit
    public static void DFS(Node node, HashSet seen){
      if(!seen.contains(node)){
        seen.add(node);
        for(var edge : node.edges){
          DFS(edge, seen);
        }
      }
    }
  }