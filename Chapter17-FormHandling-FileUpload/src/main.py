from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
import shutil

app = FastAPI()


# HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def main():
    return """
    <html>
        <body>
            <h2>Single File Upload (bytes)</h2>
            <form action="/files/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
            <h2>Single File Upload (UploadFile)</h2>
            <form action="/uploadfile/" enctype="multipart/form-data" method="post">
                <input name="file" type="file">
                <input type="submit" value="Upload">
            </form>
            <h2>Multiple Files Upload (UploadFile)</h2>
            <form action="/uploadfiles/" enctype="multipart/form-data" method="post">
                <input name="files" type="file" multiple>
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """
#--------------------------
## Return File Length not store
#--------------------------
@app.post("/files1/")
async def create_file1(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    return {"file size": len(file)}


#--------------------------
## Create File - File store with folder - selected file name not stored
#--------------------------
@app.post("/files2/")
async def create_file2(file: Annotated[bytes | None, File()] = None):
    if not file:
        return {"message": "No file sent"}
    
    filename = f"{uuid.uuid4()}.bin"
    save_path = f"uploads/{filename}"

    os.makedirs("uploads", exist_ok=True)

    with open(save_path, "wb") as buffer:
        buffer.write(file)

    return {"file size": len(file)}


#--------------------------
## UploadFile - File store with folder - selected file name is stored with original name
#--------------------------
@app.post("/uploadfile/")
async def create_upload_file(file: Annotated[UploadFile | None, File()] = None):
    if not file:
        return {"message": "No upload file sent"}
    
    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename, "content_type": file.content_type}

#-------------------------------
## Multi File Upload
#-------------------------------
@app.post("/uploadfiles/")
async def create_upload_file_multi(files: Annotated[list[UploadFile], File()]):
    save_files = []
    os.makedirs("uploads", exist_ok=True)
    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        save_files.append({"filename": file.filename})
    return save_files