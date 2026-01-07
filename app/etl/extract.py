import os
import csv
from dotenv import load_dotenv
from typing import List, Dict

load_dotenv()

DATA_DIR = os.path.join(os.getcwd(), "data")
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_rer() -> List[Dict]:
    """
    Sustituir por llamada real a la API cuando esté disponible.
    Devuelve lista de dicts listos para guardado/transformación.
    """
    return [
        {
            "numero_register": "012345",
            "nombre": "Parroquia de San Ginés",
            "confesion": "CATÓLICOS",
            "tipo_entidad": "IGLESIA",
            "municipio": "Madrid",
            "provincia": "Madrid",
            "comunidad": "MADRID"
        },
    ]

def save_to_csv(rows: List[Dict], filename: str) -> str:
    path = os.path.join(DATA_DIR, filename)
    if not rows:
        open(path, "w", encoding="utf-8-sig").close()
        return path
    with open(path, "w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return path