from sqlalchemy import Column, Integer, String, Float
from conexion_db import Base, engine  # Importamos Base y el engine desde tu archivo de conexión

# 1. Definimos una tabla de ejemplo (por ejemplo, Productos)
class Producto(Base):
    __tablename__ = "productos"  # El nombre que tendrá la tabla en phpMyAdmin

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)
    talle = Column(String(10), nullable=False)  

class Cliente(Base):
    __tablename__ = "clientes" 

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    telefono = Column(Integer, nullable=False)
    direccion = Column(String(100), nullable=False)

class Pedidos(Base):
    __tablename__ = "pedidos"    

    id = Column(Integer, primary_key=True)
    id_pedido = Column(Integer, primary_key=True)
    fecha = Column(String(50), nullable=False)
    fecha = Column(String(50), nullable=False)

# 2. Código para crear físicamente las tablas en la base de datos
if __name__ == "__main__":
    print("Creando tablas en la base de datos...")
    Base.metadata.create_all(bind=engine)
    print("¡Tablas creadas con éxito!")