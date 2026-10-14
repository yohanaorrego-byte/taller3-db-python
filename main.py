import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


def crear_conexion():
    """Lee las credenciales del archivo .env y crea el engine de SQLAlchemy."""
    load_dotenv()
    url = URL.create(
        "mysql+pymysql",
        username=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
    )
    return create_engine(url)


def main():
    engine = crear_conexion()
    with engine.connect() as conn:
        version = conn.execute(text("SELECT VERSION()")).scalar()
        print(f"Conexión exitosa. Versión de MySQL: {version}")


if __name__ == "__main__":
    main()