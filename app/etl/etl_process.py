import pandas as pd
import requests
from datetime import datetime
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app.models.models import EntidadReligiosa

def update_temporal_record(db: Session, model, codigo_field, new_data: dict):
    codigo = new_data.get(codigo_field)
    current = db.query(model).filter(
        getattr(model, codigo_field) == codigo, 
        model.valido_hasta == None
    ).first()
    
    now = datetime.utcnow()
    
    if current:
        has_changes = any(getattr(current, k) != v for k, v in new_data.items() if hasattr(current, k))
        if has_changes:
            current.valido_hasta = now
            new_version = model(**new_data, valido_desde=now)
            db.add(new_version)
    else:
        new_version = model(**new_data, valido_desde=now)
        db.add(new_version)

def run_etl():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        # Simulación de datos obtenidos del RER (Ministerio de Justicia)
        rer_data = [
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
        
        for item in rer_data:
            update_temporal_record(db, EntidadReligiosa, "numero_register", item)
            
        db.commit()
        print("ETL Entidades Religiosas completada.")
    except Exception as e:
        print(f"Error: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    run_etl()
