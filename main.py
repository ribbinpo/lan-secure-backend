import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
import aiofiles
# import shutil;
from routers import graph

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(graph.router)

# @app.post("/upload-file")
# async def create_upload_file(file: UploadFile):
#     print("filename = ", file.filename) # getting filename
#     destination_file_path = "./uploads/"+file.filename # location to store file
#     async with aiofiles.open(destination_file_path, 'wb') as out_file:
#         while content := await file.read(1024):  # async read file chunk
#             await out_file.write(content)  # async write file chunk
#     return {"Result": "OK"}

# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
