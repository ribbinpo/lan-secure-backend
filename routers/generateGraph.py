from contextlib import nullcontext
# from tkinter import image_names
from fastapi import APIRouter, File, UploadFile
import aiofiles
from graphGenerator_v2.GraphGenerator import construct_graph
from graphGenerator_v2.Visualization import visualize
from fastapi.responses import FileResponse, Response
import os

# Download Pcaps, Dots, Images

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/connected-graph/v2",
    tags=["graph"],
    responses={404: {"description": "Not found"}},
)

@router.get('/run/{pcap_path}')
async def running(pcap_path: str):
    pcap_name = pcap_path[:-5]
    node_name = pcap_name.split('_')[0]
    image_path = pcap_name + '.png'
    images_location = 'assets/images/' + node_name
    pcaps_location = 'assets/pcaps/' + node_name
    print('pcap: ', pcap_name)
    print('node: ', node_name)
    
    if pcap_path not in os.listdir(pcaps_location):
        return { "status": pcap_path + " is not Found"}
    if(node_name not in os.listdir('assets/images/')):
        print('create new ', node_name)
        # os.mkdir('assets/pcaps/'+nodeName)
        os.mkdir('assets/images/'+node_name)
        os.mkdir('assets/dots/'+node_name)
    if (image_path not in os.listdir(images_location)):
        status_graph, node_graph, edge_graph = construct_graph(pcap_name, node_name)
        status_visual, pngPath = visualize(node_graph, edge_graph, pcap_name, node_name)
        print(pcap_name,' is generated successfully')
        return {
            "file": pcap_path,
            "node": node_name,
            "file_name": pcap_name,
            "path_png": pngPath,
            "status": {
                "graph": bool(status_graph),
                "visual": bool(status_visual),
            },
        }
    return { "status": pcap_name + "\'s image and file has exist" }

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
@router.get("/getAllNode/")
async def get_file_name():
    file_list = os.listdir('assets/pcaps')
    return { "list": file_list }
# @router.get("")