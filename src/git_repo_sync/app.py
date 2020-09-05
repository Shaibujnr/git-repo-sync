from fastapi import FastAPI, Body
from typing import Any

app = FastAPI()


@app.post("/sync")
def sync(data: Any = Body(...)):
    result = {"data": data}
    print("\n\n\n")
    print(data)
    print("\n\n\n")
    return result
