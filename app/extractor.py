import requests
from bs4 import BeautifulSoup

def extraer_conversacion(url: str) -> list[str]:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    mensajes = []

    for bloque in soup.find_all("div"):
        texto = bloque.get_text(strip=True)
        if texto and len(texto) > 20:
            mensajes.append(texto)

    return mensajes
