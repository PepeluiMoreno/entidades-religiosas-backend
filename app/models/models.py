from sqlalchemy import Column, String, Integer, DateTime, Date
from app.database import Base
from datetime import datetime

class TemporalModel:
    valido_desde = Column(DateTime, default=datetime.utcnow, nullable=False)
    valido_hasta = Column(DateTime, nullable=True)

class EntidadReligiosa(Base, TemporalModel):
    __tablename__ = "entidades_religiosas"
    id_version = Column(Integer, primary_key=True, autoincrement=True)
    numero_register = Column(String, index=True, nullable=False)
    nombre = Column(String, nullable=False)
    confesion = Column(String)
    subconfesion = Column(String)
    tipo_entidad = Column(String)
    municipio = Column(String)
    provincia = Column(String)
    comunidad = Column(String)
    fecha_inscripcion = Column(Date)
