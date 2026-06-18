from typing import List, Tuple, Dict
from dataclasses import dataclass
import heapq

@dataclass
class NetworkEdge:
    to_server: str
    latency_ms: int

@dataclass
class Server:
    label: str
    edges: List[NetworkEdge] = []

    def add_edge(self, edge: NetworkEdge):
        self.edges.append(edge)

    def sync_file_changes(self, file_id: str):
        # Placeholder method for syncing file changes
        print(f"Syncing file changes for file_id: {file_id} on server {self.label}")

class NetworkGraph:
    def __init__(self):
        self.servers: Dict[str, Server] = {}

    def add_server(self, label: str):
        self.servers[label] = Server(label)
    
    def add_link(self, server_u_label: str, server_v_label: str, latency_ms: int):
        server_u = self.servers.get(server_u_label, None)
        server_v = self.servers.get(server_v_label, None)

        if server_u is None or server_v is None:
            return
        
        server_u.add_edge(NetworkEdge(server_v_label, latency_ms))
        server_v.add_edge(NetworkEdge(server_u_label, latency_ms))

    def get_sync_path(self, start_server: str) -> List[Tuple[str, str]]:
        visited: Dict[Server, bool] = {server: False for server in self.servers.values()}
        min_heap: List[Tuple[int, Server, str]] = [(0, self.servers[start_server], None)]
        mst: List[Tuple[str, str]] = []

        while min_heap:
            latency, server, parent = heapq.heappop(min_heap)

            if not visited[server]:
                visited[server] = True
                if parent is not None:
                    mst.append((parent, server.label))
                
                for edge in server.edges:
                    next_server = self.servers[edge.to_server]
                    if not visited[next_server]:
                        heapq.heappush(min_heap, (edge.latency_ms, next_server, server))

        return mst
    
    def broadcast_update(self, file_id: str, start_server: str):
        sync_path: List[Tuple[str, str]] = self.get_sync_path(start_server)

        for _, to_server in sync_path:
            next_server = self.servers[to_server]
            next_server.sync_file_changes(file_id)
            
            
            # The Problem: "The Distributed Data Sync (Mirroring)"

# Imagine you are building a system like Dropbox or Google Drive Desktop. You have a cluster of "Edge Servers"
# across the globe. Some servers are connected to each other via high-speed fiber, forming a network (a Graph).

# **The Task:**
# You need to implement a "Synchronization Manager" that ensures a data update (a file change) originating 
# at Server A reaches all other servers in the network as quickly as possible, while using the minimum number
# of network links (to save cost/bandwidth).

# **The API:**

# 1. add_link(server_u: str, server_v: str, latency_ms: int):

# - Adds a bidirectional network connection between two servers with a specific cost (latency).

# 2. get_sync_path(start_server: str) -> List[Tuple[str, str]]:

# - Returns a list of links (edges) that form a Minimum Spanning Tree (MST). This ensures every server is 
# connected with the lowest possible total latency.

# 3. broadcast_update(file_id: str, start_server: str):

# - Initiates the sync process across the calculated path.

# ---

# ## Phase 1: Single machine 

# # ### Approach

# # - Graph representation: Use an adjacency list to represent the network of servers and their connections.
# # - Algorithm: Use prim's algorithm to compute the minimum spanning tree (MST) of the graph,
# as it expands outward from a node and is efficient for dense graphs.

# # ### Implementation Steps:

# # - Implement the `add_link` method to build the graph.
# # - Implement the `get_sync_path` method to compute the MST using Prim's algorithm.
# #     - Add the starting server to a priority queue.
# #     - While the priority queue is not empty, pop the server with the lowest latency.
# #     - For each neighbor of the popped server, if it is not already in the MST, add it to the priority 
# queue with its latency.
# #     - Continue until all servers are included in the MST.
# #     - Return the edges of the MST as a list of tuples.
# # - Implement the `broadcast_update` method to simulate the propagation of a file update across the MST.
# #     - Start from the `start_server` and traverse the MST, sending the update to each connected server.
# #     - Ensure that each server only receives the update once.