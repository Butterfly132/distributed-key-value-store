from fastapi import FastAPI

app = FastAPI()

# This dictionary is our in-memory database
store = {}

@app.get("/")
def home():
    return {"message": "KV Store is running"}

@app.put("/put/{key}")
def put_value(key: str, value: str):
    store[key] = value
    return {"message": "Value stored successfully"}

@app.get("/get/{key}")
def get_value(key: str):
    if key not in store:
        return {"error": "Key not found"}
    return {"value": store[key]}
