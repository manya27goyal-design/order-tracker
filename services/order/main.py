from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Order Service")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}


class Item(BaseModel):
    name: str
    price: float
    quantity: int = 1


@app.post("/items/echo")
def echo_item(item: Item):
    return {"received": item, "total": item.price * item.quantity}