from fastapi import APIRouter
from graphGenerator.GraphGenerator import construct_graph
from graphGenerator.Visualization import visualize

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/connected-graph",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
async def read_root():
    fileName = 'a004_20220210_000001'
    status_graph, node_graph, edge_graph = construct_graph(fileName)
    status_visual, pngPath = visualize(node_graph, edge_graph, fileName)
    return { "status": status_visual, "png": pngPath  }
@router.get('/{pcap_name}')
async def read_pcap(pcap_name: str):
    return [{ "pcap_name": pcap_name }]