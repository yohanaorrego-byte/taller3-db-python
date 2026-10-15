import os

from dotenv import load_dotenv
from faker import Faker
from sqlalchemy import (Column, Date, Integer, MetaData, String, Table,
                        create_engine, delete, func, insert, select)
from sqlalchemy.engine import URL

NOMBRE_TABLA = "personas_yohana"
TOTAL_REGISTROS = 100_000
TAMANO_LOTE = 5_000


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


def generar_lote(fake, cantidad):
    """Genera una lista de diccionarios con datos falsos."""
    return [
        {
            "nombre": fake.first_name(),
            "apellido": fake.last_name(),
            "correo": fake.email(),
            "telefono": fake.phone_number(),
            "fecha_nacimiento": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "ciudad": fake.city(),
            "direccion": fake.address().replace("\n", ", "),
            "profesion": fake.job(),
            "empresa": fake.company(),
        }
        for _ in range(cantidad)
    ]


def main():
    engine = crear_conexion()
    metadata = MetaData()
    tabla = definir_tabla(metadata)
    metadata.create_all(engine)  # crea la tabla solo si no existe

    fake = Faker("es_CO")

    with engine.begin() as conn:
        conn.execute(delete(tabla))  # evita duplicados si se ejecuta dos veces
        insertados = 0
        while insertados < TOTAL_REGISTROS:
            cantidad = min(TAMANO_LOTE, TOTAL_REGISTROS - insertados)
            conn.execute(insert(tabla), generar_lote(fake, cantidad))
            insertados += cantidad
            print(f"Insertados: {insertados}/{TOTAL_REGISTROS}")

        total = conn.execute(select(func.count()).select_from(tabla)).scalar()
        print(f"Total en la tabla {NOMBRE_TABLA}: {total}")


if __name__ == "__main__":
    main()