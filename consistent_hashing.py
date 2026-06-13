from dataclasses import dataclass
from typing import List, Dict
import bisect
import hashlib

@dataclass
class Server:
    id: str

class ConsistentHashing:
    def __init__(self, servers: List[Server], num_replicas: int = 3):
        self.servers: Dict[str, Server] = {}
        self.num_replicas = num_replicas
        self.hash_to_server: Dict[int, str] = {}
        self.ring = []
        for server in servers:
            self.servers[server.id] = server
        self._build_ring()

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), 16)
    
    def _build_ring(self):
        for server in self.servers.values():
            for replica in range(self.num_replicas):
                server_id = f"{server.id}#{replica}"
                hash = self._hash(server_id)
                self.ring.append(hash)
                self.hash_to_server[hash] = server.id
        self.ring.sort()
    
    def get_server(self, key: str) -> Server:
        if not self.ring:
            return None
        
        hash = self._hash(key)
        
        idx = bisect.bisect(self.ring, hash) % len(self.ring)
        hash_val = self.ring[idx]
        return self.servers[self.hash_to_server[hash_val]]
    
    def add_server(self, server: Server):
        if server.id in self.servers:
            return

        self.servers[server.id] = server
        for replica in range(self.num_replicas):
            server_id = f"{server.id}#{replica}"
            hash_val = self._hash(server_id)
            bisect.insort(self.ring, hash_val)
            self.hash_to_server[hash_val] = server.id

    def remove_server(self, server_id: str):
        if server_id not in self.servers:
            return

        for replica in range(self.num_replicas):
            replica_id = f"{server_id}#{replica}"
            hash_val = self._hash(replica_id)
            self.ring.remove(hash_val)
            del self.hash_to_server[hash_val]

        del self.servers[server_id]

def main():
    servers: List[Server] = [Server("S0"), Server("S1"), Server("S2"), Server("S3"), Server("S4"), Server("S5")]
    consistent_hashing = ConsistentHashing(servers)
    print("Original assignment")
    print(consistent_hashing.get_server("UserA"))
    print(consistent_hashing.get_server("UserB"))

    consistent_hashing.add_server(Server("S6"))
    print("After adding server S6")
    print(consistent_hashing.get_server("UserA"))
    print(consistent_hashing.get_server("UserB"))
    
    print('After removing server S4')
    consistent_hashing.remove_server("S4")
    print(consistent_hashing.get_server("UserA"))
    print(consistent_hashing.get_server("UserB"))

if __name__ == '__main__':
    main()
        