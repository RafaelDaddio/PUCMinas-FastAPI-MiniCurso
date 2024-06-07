from fastapi import FastAPI

from app.modules.first_example.routes import route as first_example_router
from app.modules.cliente.routes import router as cliente_router


def create_routes(app: FastAPI) -> None:

    app.include_router(first_example_router, tags=['First Example!'])
    app.include_router(cliente_router, tags=["Cliente"])
