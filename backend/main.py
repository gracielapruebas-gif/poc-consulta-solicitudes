
from fastapi import FastAPI, HTTPException

app = FastAPI(
    title="API Consulta de Solicitudes",
    version="1.0.0"
)

solicitudes = {
    "SOL-1024": {
        "id": "SOL-1024",
        "estado": "En revisión",
        "area": "Soporte",
        "responsable": "Equipo de Soporte",
        "fecha_estimada": "28-11-2026",
        "usuario_id": "usuario001"
    },
    "SOL-1025": {
        "id": "SOL-1025",
        "estado": "En proceso",
        "area": "Tecnología",
        "responsable": "Equipo de Desarrollo",
        "fecha_estimada": "30-11-2026",
        "usuario_id": "usuario002"
    }
}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/solicitudes/{solicitud_id}")
def consultar_solicitud(solicitud_id: str):
    solicitud = solicitudes.get(solicitud_id.upper())

    if not solicitud:
        raise HTTPException(
            status_code=404,
            detail="Solicitud no encontrada"
        )

    # Solo para prueba local.
    # La autorización real se implementará
    # utilizando la identidad autenticada.
    return solicitud
