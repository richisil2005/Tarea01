from fastapi import FastAPI, HTTPException
from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel

app = FastAPI()

class Producto(BaseModel):
    id: Optional[UUID] = None
    name: Optional[str] = None
    descrip: Optional[str] = None
    price: Optional[float] = None 
    stock: Optional[int] = None 

productos = []

@app.post("/productos") #sirve
def crear_producto(producto: Producto):
    producto.id = uuid4()
    productos.append(producto.dict())
    return producto

@app.put("/productos/{producto_id}") #sirve
def cambiar_producto(producto_id: UUID,producto: Producto):
    for prod in productos:
        if prod["id"] == producto_id:
            productos.remove(prod)
            productos.append(producto.dict())
            return {"message": "Producto actualizado completamente"}

@app.delete("/productos/{producto_id}") #sirve
def eliminar_producto(producto_id: UUID):
    for prod in productos:
        if prod["id"] == producto_id:
            productos.remove(prod)

@app.get("/productos") #sirve
def obtener_productos():
    return productos

@app.get("/productos/{producto_id}") #sirve
def obtener_producto(producto_id: UUID):
    for prod in productos:
        if prod["id"] == producto_id:
            return prod

@app.patch("/productos/{producto_id}")
def modificar_producto(producto_id: UUID,producto:Producto):
    for i in range(len(productos)):
        if productos[i].id == producto_id:
            if producto.name:
                productos[i].name = producto.name
            if producto.descrip:
                productos[i].descrip = producto.descrip
            if producto.precio:
                productos[i].price = producto.price
            if producto.stock:
                productos[i].stock = producto.stock    
            return productos[i]
    return "Producto no encontrado"