from fastapi import FastAPI

from app.modules.first_example.routes import route as first_example_router
from app.modules.cliente.routes import router as cliente_router
from app.modules.filme.routes import router as filme_router


def create_routes(app: FastAPI) -> None:

    app.include_router(first_example_router, tags=['First Example!'])
    app.include_router(cliente_router, tags=["Cliente"])
    app.include_router(filme_router, tags=['Filmes'])
