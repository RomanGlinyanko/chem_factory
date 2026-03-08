from fastapi import FastAPI
from .routes import routers

app = FastAPI(title = 'chem_fact')
for router in routers:
    app.include_router(router)
