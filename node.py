import sys
import hashlib
from fastapi import FastAPI
import requests

app = FastAPI()

# Each node has its own storage
store = {}

# Read port number from command line
NODE_PORT = int(sys.argv[1])

# List of all nodes in the system
NODES = [8001, 8002, 8003]

def get_replica_nodes(key: str):
    hash_value = int(hashlib.sha256(key.encode()).hexdigest(), 16)
    index = hash_value % len(NODES)

    primary = NODES[index]
    replica = NODES[(index + 1) % len(NODES)]

    return primary, replica


@app.get("/")
def home():
    return {"message": f"Node running on port {NODE_PORT}"}

@app.put("/put/{key}")
def put_value(key: str, value: str):
    primary, replica = get_replica_nodes(key)

    # Forward to primary if needed
    if NODE_PORT != primary:
        requests.put(
            f"http://127.0.0.1:{primary}/put/{key}",
            params={"value": value}
        )
        return {"message": f"Forwarded to primary node {primary}"}

    # Store locally (primary)
    store[key] = value

    # Send replica copy
    if replica != NODE_PORT:
        requests.put(
            f"http://127.0.0.1:{replica}/replica/{key}",
            params={"value": value}
        )

    return {"message": "Stored on primary and replicated"}
@app.put("/replica/{key}")
def replica_put(key: str, value: str):
    store[key] = value
    return {"message": "Replica stored"}


@app.get("/get/{key}")
def get_value(key: str):
    primary, replica = get_replica_nodes(key)

    # Try primary first
    if NODE_PORT != primary:
        try:
            response = requests.get(
                f"http://127.0.0.1:{primary}/get/{key}",
                timeout=1
            )
            return response.json()
        except:
            # Primary failed → try replica
            response = requests.get(
                f"http://127.0.0.1:{replica}/get/{key}"
            )
            return response.json()

    # Local read
    return {"value": store.get(key)}


    return {"value": store.get(key)}
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=NODE_PORT)
