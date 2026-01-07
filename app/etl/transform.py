from typing import List, Dict

def transform_rer(rows: List[Dict]) -> List[Dict]:
    """
    Transformación mínima: normaliza strings (strip) y deja en mayúsculas
    los campos tipo texto para consistencia. Ajustar según necesidades.
    """
    out: List[Dict] = []
    for r in rows:
        nr = {k: (v.strip().upper() if isinstance(v, str) else v) for k, v in r.items()}
        out.append(nr)
    return out