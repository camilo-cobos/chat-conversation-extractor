from docx import Document

def generar_txt(mensajes: list[str], ruta: str):
    with open(ruta, "w", encoding="utf-8") as f:
        for mensaje in mensajes:
            f.write(mensaje + "\n\n")


def generar_docx(mensajes: list[str], ruta: str):
    doc = Document()
    for mensaje in mensajes:
        doc.add_paragraph(mensaje)
    doc.save(ruta)

