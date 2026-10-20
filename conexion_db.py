import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Cargamos las variables del archivo .env
load_dotenv()

# Leemos los datos de configuración
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construimos la URL de conexión para MySQL
URL_DATABASE = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Creamos el motor de la base de datos
engine = create_engine(URL_DATABASE)

# Sesión para futuras consultas del backend
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para definir los modelos de las tablas
Base = declarative_base()

# Prueba de conexión
if __name__ == "__main__":
    try:
        connection = engine.connect()
        print("¡Conexión exitosa a la base de datos Retoke-Jeans!")
        connection.close()
    except Exception as error:
        print("Error al conectar a la base de datos:", error)