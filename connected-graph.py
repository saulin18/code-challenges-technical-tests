#Task
#Your mission is to write the function that checks whether the provided segments form a graph.
#
#Ins/Out
#This function receive an array of Segments as parameter and should return:
#
#true if all the Segments are connected as a single graph.
#Basically, if each and every points of all Segments are reachable from any other points.
#false if the previous is not verified
#Properties
#A Segment is an object containing 2 properties: a and b.
#Both have a Point assigned.
#
#A Point is an object containing 2 properties: x and y.
#Both containing an Integer and representing coordinates of the Point
#
#AlgorithmsGraph Theory


from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

@dataclass
class Segment:
    a: Point
    b: Point

def is_one_graph(input_segments: list[Segment]) -> bool:
    
    if not input_segments:
        return True
    
    adj_list = {}
    
    def build_adj_list(adj_list, input_segments):
        for i, segment in enumerate(input_segments):
            a = (segment.a.x, segment.a.y)
            b = (segment.b.x, segment.b.y)
            
            if a not in adj_list:
                adj_list[a] = []
            if b not in adj_list:
                adj_list[b] = []
            
            adj_list[a].append(b)
            adj_list[b].append(a)
    
    build_adj_list(adj_list, input_segments)        
            
    seen = set()
          
    def dfs(node, seen):
     if node in seen:
        return
     seen.add(node)
     for neighbor in adj_list.get(node, []):
        dfs(neighbor, seen)
        
    first_node = (input_segments[0].a.x, input_segments[0].a.y)
    dfs(first_node, seen)
    
    return len(seen) == len(adj_list)    
        
                
    

