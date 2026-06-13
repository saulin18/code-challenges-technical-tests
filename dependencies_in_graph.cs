//
// Expanding Dependency Chains
// When building a program a file only needs to be compiled if it or one of its dependencies
// has changed since the last build. However, these changes can propogate upwards through 
// dependencies. For example, if A is dependent on B, and B is dependent on C, then a change
// to C will require that all three files be recompiled.//
// For this kata you will be provided with a list of files along with their immediate 
// dependencies. Your task is to determine all dependencies for every file in the list,
// and return those values.//
// Specification:
// Your code needs to accept as its input a Dictionary<string,string[]> The keys 
// in the dictionary contain the names of the files you need to consider as strings.
// Each key (file) is mapped to an array of strings, each element of which represents
// a single direct dependency. A file with no dependencies is mapped to an empty array.//
// The return from your method needs to follow the same format, a Dictionary<string,string[]>
// mapping file names to dependencies, but needs to include all the dependencies, 
// not just the direct dependencies.//
// You will also need to check for circular dependencies. For example, if you have three
// files, A, B, and C, with A dependent on B, B dependent on C, and C dependent on A, 
// there is a circular dependency. In such cases you should throw an InvalidOperationException.//
// Example:
// As input for our example I have provided a dictionary detailing 4 files, A, B, C,
// and D. A is dependent on B and D. B is dependent on C, and C and dependent on D.
// "A" => ["B", "D"]
// "B" => ["C"]
// "C" => ["D"]
// "D" => [ ]
// When we expand these out we come up with a new set up dependencies:
// "A" => ["B", "C", "D"]
// "B" => ["C", "D"]
// "C" => ["D"]
// "D" => [ ]
// Because B is dependent on C and, indirectly, D, those are added to A as well. 
// The order isn't important in 
// your results, but even files with no dependencies still need to remain in the list.

using System;
using System.Linq;
using System.Collections.Generic;

public class Kata {

  //To represent the state while we are traversing the graph, 
  // for detecting circular dependencies (cycle)
  public enum DependenciesState
  {
    NotVisited,
    Visiting,
    Visited
  }

  public class Graph
  {
    public Dictionary<string, string[]> Dependencies { get; set; }

    public Graph(Dictionary<string, string[]> dependencies)
    {
      Dependencies = dependencies;
    }

    public void AddDependency(string file, string[] dependencies)
    {
      Dependencies[file] = dependencies;
    }

    public bool hasCycle()
    {
      //Reset the state of the graph
      var state = new Dictionary<string, DependenciesState>();
      foreach (var dependency in Dependencies)
      {
        state[dependency.Key] = DependenciesState.NotVisited;
      }

      foreach (var dependency in Dependencies.Keys)
      {
        if (state[dependency] == DependenciesState.NotVisited)
        {
          if (isCyclePresent(dependency, state))
          {
            return true;
          }
        }
      }
      return false;
    }

    private bool isCyclePresent(string file, Dictionary<string, DependenciesState> state)
    {
      if (state[file] == DependenciesState.Visiting)
      {
        return true;
      }
      state[file] = DependenciesState.Visiting;
      foreach (var dependency in Dependencies[file])
      {

        if (state[dependency] == DependenciesState.Visiting)
        {
          return true;
        }

        if (state[dependency] == DependenciesState.NotVisited)
        {

          if (isCyclePresent(dependency, state))
          {
            return true;
          }
        }
      }
      state[file] = DependenciesState.Visited;
      return false;
    }
    
      public List<string> topologicalSort(Dictionary<string, string[]> dependencies)
  {
    var result = new List<string>();
    var nodeStates = new Dictionary<string, DependenciesState>();
    
    if(hasCycle())
    {
      throw new InvalidOperationException("Cycle detected in the dependencies");
    }

  //Reset the state of the graph
    foreach (var node in dependencies.Keys)
    {
      nodeStates[node] = DependenciesState.NotVisited;
    }
    
    //Call the recursive function for doing DFS on every node
    foreach (var node in dependencies.Keys)
    {
      if (nodeStates[node] == DependenciesState.NotVisited)
      {
        doTopologicalSort(node, nodeStates, result);
      }
    }

    return result;
  }

  public void doTopologicalSort(string node, Dictionary<string, DependenciesState> nodeStates, List<string> result)
  {
    nodeStates[node] = DependenciesState.Visiting;
    foreach (var dependency in Dependencies[node])
    {
      if (nodeStates[dependency] == DependenciesState.NotVisited)
      {
        doTopologicalSort(dependency, nodeStates, result);
      }
    }
    nodeStates[node] = DependenciesState.Visited;
    result.Add(node);
  }

  }


  public static Dictionary<string, string[]> ExpandDependencies(Dictionary<string, string[]> dependencies)
  {
    var graph = new Graph(dependencies);
    var order = graph.topologicalSort(dependencies);
    var expandedDependencies = new Dictionary<string, List<string>>();
    var currentSet = new HashSet<string>();
    foreach (var node in order)
    {

      foreach (var dep in graph.Dependencies[node])
      {
        currentSet.Add(dep);
        currentSet.UnionWith(expandedDependencies[dep]);
      }
     expandedDependencies[node] = currentSet.ToList();
     currentSet.Clear();
    }
    return expandedDependencies.ToDictionary(x => x.Key, x => x.Value.ToArray());
  }
} 