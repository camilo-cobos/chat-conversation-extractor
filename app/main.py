from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse
import uuid
import os

from app.extractor import extraer_conversacion
from app.file_generator import generar_txt, generar_docx

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()


@app.post("/extraer")
def extraer(
    url: str = Form(...),
    formato: str = Form(...)
):
    mensajes = extraer_conversacion(url)

    nombre = f"conversacion_{uuid.uuid4()}"

    if formato == "docx":
        ruta = f"{nombre}.docx"
        generar_docx(mensajes, ruta)
    else:
        ruta = f"{nombre}.txt"
        generar_txt(mensajes, ruta)

    return FileResponse(
        ruta,
        filename=ruta,
        media_type="application/octet-stream"
    )
