from fastapi import FastAPI
from .database import engine, Base
from .routers import usuarios, proyectos, bitacora, log, gasolineras, rol, vehiculos

app = FastAPI()

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(usuarios.router, prefix="/usuarios", tags=["usuarios"])
app.include_router(proyectos.router, prefix="/proyectos", tags=["proyectos"])
app.include_router(bitacora.router, prefix="/bitacora", tags=["bitacora"])
app.include_router(log.router, prefix="/log", tags=["log"])
app.include_router(gasolineras.router, prefix="/gasolineras", tags=["gasolineras"])
app.include_router(rol.router, prefix="/rol", tags=["rol"])
app.include_router(vehiculos.router, prefix="/vehiculos", tags=["vehiculos"])

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de UES GASOLINERA"}
