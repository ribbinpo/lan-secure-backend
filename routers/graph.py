from tkinter import image_names
from fastapi import APIRouter, File, UploadFile
import aiofiles
from graphGenerator.GraphGenerator import construct_graph
from graphGenerator.Visualization import visualize
from fastapi.responses import FileResponse, Response

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/connected-graph",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

# show dot file, save to png file
@router.get('/{pcap_name}')
async def read_pcap(pcap_name: str):
    return [{ "pcap_name": pcap_name }]

@router.get('/run/{pcap_name}')
async def running(pcap_name: str):
    pcapsPath = "assets/pcaps/"+ pcap_name
    status_graph, node_graph, edge_graph = construct_graph(pcapsPath)
    status_visual, pngPath = visualize(node_graph, edge_graph, pcapsPath)
    return {
        "Graph's status: ": status_graph,
        "Visual's status": status_visual    
    }

@router.get('/uploadImage/{image_name}')
async def downloadImage(image_name: str):
    pcapsPath = "assets/pcaps/"+ image_name
    return FileResponse(path=pcapsPath, filename=pcapsPath)

# upload file pcap
@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    if not file:
        return { "message": "No upload file sent" }
    print("filename = ", file.filename) # getting filename
    pcapsPath = "assets/pcaps/"+file.filename # location to store file
    async with aiofiles.open(pcapsPath, 'wb') as out_file:
        while content := await file.read(1024):
            await out_file.write(content)
    status_graph, node_graph, edge_graph = construct_graph(file.filename)
    # Cut .pcap file name
    status_visual, pngPath = visualize(node_graph, edge_graph, file.filename)
    return { "Result": status_visual }

# @router.get('/')
# async def read_root():
#     fileName = 'a004_20220210_000001.pcap'
#     status_graph, node_graph, edge_graph = construct_graph(fileName)
#     status_visual, pngPath = visualize(node_graph, edge_graph, fileName)
#     return { "status": status_visual, "png": pngPath  }
