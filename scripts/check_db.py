import os
from pathlib import Path
from dotenv import load_dotenv
import psycopg2

# load .env from repo root
root = Path(__file__).resolve().parents[1]
load_dotenv(root / ".env")

db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise SystemExit("DATABASE_URL no definido en .env")

sync_url = db_url.replace("+asyncpg", "").strip().strip('"').strip("'")

conn = psycopg2.connect(sync_url)
try:
    cur = conn.cursor()
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_name='opendata'")
    print("schema opendata:", cur.fetchall())
    cur.execute("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname='opendata'")
    print("tables in opendata:", cur.fetchall())
    cur.execute("SELECT version_num FROM alembic_version")
    print("alembic_version:", cur.fetchall())
    cur.close()
finally:
    conn.close()