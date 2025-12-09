from fastapi import FastAPI

from app.api.routes.auth import router as auth_router
from app.db.session import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Reservation Auth")

app.include_router(auth_router, prefix="", tags=["auth"])
