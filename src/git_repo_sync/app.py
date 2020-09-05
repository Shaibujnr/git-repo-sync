from fastapi import FastAPI

app = FastAPI()


@app.post("/sync")
def sync():
    return {"hello": "world"}
