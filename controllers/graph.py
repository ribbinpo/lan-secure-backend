from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from typing import Optional
from fastapi import Query
from graph_generator.GraphGenerator import construct_graph

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/connected-graph",
    tags=["ConnectedGraph"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def read_root():
    fileName = 'a004_20220210_000001'
    stat, V, E = construct_graph('assets/pcaps/'+fileName+'.pcap')
    return { "stat":stat, "V": V, "E": E }
@router.get('/{pcap_name}')
async def read_pcap(pcap_name: str):
    return [{ "pcap_name": pcap_name }]