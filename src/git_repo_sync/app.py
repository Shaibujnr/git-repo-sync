from fastapi import FastAPI, Body
from typing import Any

app = FastAPI()


@app.post("/target")
def sync(url: str, username: str, token: str, data: Any = Body(...)):
    result = {"data": data}
    print("\n\n\n")
    print(data)
    print(f"url: {url}")
    print(f"username: {username}")
    print(f"token: {token}")
    print("\n\n\n")
    return result
