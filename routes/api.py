from pkg_resources import ResolutionError
from fastapi import APIRouter
from controllers import graph

router = APIRouter()

router.include_router(graph.router)