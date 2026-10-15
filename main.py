import os

from dotenv import load_dotenv
from sqlalchemy import (Column, Date, Integer, MetaData, String, Table,
                        create_engine)
from sqlalchemy.engine import URL

NOMBRE_TABLA = "personas_yohana"


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


def definir_tabla(metadata):
    """Define la estructura de la tabla de personas."""
    return Table(
        NOMBRE_TABLA, metadata,
        Column("id", Integer, primary_key=True, autoincrement=True),
        Column("nombre", String(100)),
        Column("apellido", String(100)),
        Column("correo", String(150)),
        Column("telefono", String(40)),
        Column("fecha_nacimiento", Date),
        Column("ciudad", String(100)),
        Column("direccion", String(255)),
        Column("profesion", String(150)),
        Column("empresa", String(150)),
    )


def main():
    engine = crear_conexion()
    metadata = MetaData()
    definir_tabla(metadata)
    metadata.create_all(engine)  # crea la tabla solo si no existe
    print(f"Tabla {NOMBRE_TABLA} lista.")


if __name__ == "__main__":
    main()