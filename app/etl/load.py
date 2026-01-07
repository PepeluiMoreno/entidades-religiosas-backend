import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def _sync_db_url(db_url: str) -> str:
    # Convierte URLs tipo SQLAlchemy async (ej. postgresql+asyncpg://) a sync para psycopg2
    return db_url.replace("+asyncpg", "")

def copy_csv_to_table(csv_path: str, table: str, schema: str | None = None):
    """
    Copia un CSV (con cabecera) directamente a una tabla PostgreSQL usando COPY.
    Usa DATABASE_URL y opcionalmente DATABASE_SCHEMA de .env. Lanza RuntimeError si falta DATABASE_URL.
    """
    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL no definido en .env")
    if schema is None:
        schema = os.getenv("DATABASE_SCHEMA", "opendata")
    sync_url = _sync_db_url(db_url)
    with open(csv_path, "r", encoding="utf-8-sig") as fh:
        header = fh.readline().strip()
        cols = [c.strip() for c in header.split(",") if c.strip()]
        fh.seek(0)
        copy_sql = f"COPY {schema}.{table} ({', '.join(cols)}) FROM STDIN WITH CSV HEADER DELIMITER ','"
        conn = psycopg2.connect(sync_url)
        try:
            cur = conn.cursor()
            cur.copy_expert(copy_sql, fh)
            conn.commit()
        finally:
            conn.close()



            