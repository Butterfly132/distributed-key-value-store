# Distributed Key-Value Store

A distributed key-value store implemented in **Python** using **FastAPI**, supporting **data partitioning, replication, and fault tolerance**.  
This project demonstrates core concepts of **distributed systems** such as hashing-based data distribution, request forwarding, and recovery from node failures.

---

## 📌 Problem Statement

Modern large-scale systems (like Amazon DynamoDB) need to:
- Store massive amounts of data
- Distribute data across multiple servers
- Remain available even if some servers fail

This project solves a simplified version of that problem by building a distributed key-value store that:
- Distributes keys across multiple nodes
- Replicates data for fault tolerance
- Automatically routes requests to the correct node

---

## 🏗️ System Architecture

- Multiple backend nodes run on different ports (8001, 8002, 8003)
- Each node runs the same application code
- A hashing function determines which node owns a key
- Each key is stored on:
  - **Primary node**
  - **Replica node (backup)**


---

## 🔑 Key Concepts Implemented

### 1️⃣ Data Partitioning (Hashing)
- SHA-256 hashing is used to map keys to nodes
- Same key always maps to the same primary node
- Ensures even distribution of data across nodes

### 2️⃣ Request Forwarding
- Clients can send requests to **any node**
- If the node is not responsible for the key, the request is forwarded automatically
- This makes the system transparent to the client

### 3️⃣ Replication
- Each key is stored on two nodes:
  - Primary
  - Replica
- Improves data availability and reliability

### 4️⃣ Fault Tolerance
- If the primary node fails:
  - The system automatically reads from the replica
- Ensures data availability during node crashes

---

## 🚀 How to Run the Project Locally

### Prerequisites
- Python 3.10+
- pip

### Setup
```bash
python -m venv venv
venv\Scripts\activate   # Windows
pip install fastapi uvicorn requests
Start the Nodes (in separate terminals)
python node.py 8001
python node.py 8002
python node.py 8003

Access APIs

Open Swagger UI in browser:

http://127.0.0.1:8001/docs
http://127.0.0.1:8002/docs
http://127.0.0.1:8003/docs

🧪 Fault Tolerance Demonstration

Insert a key-value pair using any node

Stop the primary node (Ctrl + C)

Fetch the key from another node

Data is successfully returned from the replica node

This demonstrates successful replication and failure recovery.

🛠️ Tech Stack

Python

FastAPI

Uvicorn

REST APIs

Hashing (SHA-256)

📈 Limitations & Future Improvements

In-memory storage (no persistence)

No dynamic node addition/removal

Eventual consistency model

Future enhancements:

Persistent storage (disk/database)

Consistent hashing ring

Leader election

Health checks and monitoring

🎯 Key Learnings

Fundamentals of distributed systems

Data partitioning and replication strategies

Designing systems to handle failures

Building and testing multi-node backend services locally

📎 Author

Ishita Singh
GitHub: https://github.com/Butterfly132
