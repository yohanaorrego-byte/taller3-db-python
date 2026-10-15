# Taller U3: Automatización de BD con Python, Faker y Git

Script en Python que se conecta a una base de datos MySQL local con SQLAlchemy, crea la tabla `personas_yohana` si no existe y la llena con 100.000 registros generados con Faker, insertados por lotes de 5.000.

## Requisitos
- Python 3.10 o superior
- MySQL en ejecución local (por ejemplo, con WampServer)
- DBeaver (para verificar los datos)

## Instalación
```bash
git clone https://github.com/yohanaorrego-byte/taller3-db-python.git
cd taller3-db-python
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Configuración
1. Crea la base de datos en MySQL: `CREATE DATABASE taller3_db;`
2. Copia `.env.example` a `.env` y escribe tus credenciales reales.

## Ejecución
```bash
python main.py
```

## Estructura de la tabla `personas_yohana`
id (PK), nombre, apellido, correo, telefono, fecha_nacimiento, ciudad, direccion, profesion, empresa.

## Verificación
```sql
SELECT COUNT(*) FROM personas_yohana;
```