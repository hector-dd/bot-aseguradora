from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

# ===== CONFIG =====
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ===== FUNCION PARA BUSCAR CLIENTE =====
def buscar_cliente(valor):
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{GOOGLE_SHEET_ID}/values/prueba%20polizas!A:Z?key={GOOGLE_API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    if "values" not in data:
        return {"error": "No se pudieron obtener datos del Sheet"}

    filas = data["values"]

    for fila in filas:
        if valor.lower() in [celda.lower() for celda in fila]:
            return {
                "cliente": fila[0],
                "poliza": fila[1],
                "telefono": fila[2],
                "estatus": fila[3]
            }

    return {"mensaje": "Cliente no encontrado"}

# ===== ENDPOINT PRINCIPAL =====
@app.get("/buscar")
def home():
    return {"mensaje": "Servidor funcionando 🔥"}

# ===== ENDPOINT DE BUSQUEDA =====
@app.get("/buscar")
def buscar(valor: str):
    return buscar_cliente(valor)