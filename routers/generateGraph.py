from tkinter import image_names
from fastapi import APIRouter, File, UploadFile
import aiofiles
from graphGenerator_v2.GraphGenerator import construct_graph
from graphGenerator_v2.Visualization import visualize
from fastapi.responses import FileResponse, Response
import os

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/connected-graph/v2",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

@router.get('/run/{pcap_name}')
async def running(pcap_name: str):
    pcapsPath = pcap_name
    status_graph, node_graph, edge_graph = construct_graph(pcapsPath)
    status_visual, pngPath = visualize(node_graph, edge_graph, pcapsPath)
    return {
        "Graph's status: ": status_graph,
        "Visual's status": status_visual    
    }

@router.get('/download/{file_name}')
async def downloadImage(file_name: str):
    pcapsPath = "assets/pcaps/"+ file_name
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
@router.get("/getname/")
async def get_file_name():
    file_list = os.listdir('assets/pcaps')
    return { "list": file_list }
