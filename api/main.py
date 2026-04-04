from fastapi import FastAPI, File, UploadFile

from api.processing import convert_document

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Revision AI"}

@app.post("/file-processing")
async def file_processing(file: UploadFile = File(...)):
    data = await file.read()
    markdown = convert_document(data, file.filename or "upload.bin")[0]
    chunks = convert_document(data, file.filename or "upload.bin")[1]
    return {
        "message": "File Processed",
        "fileName": file.filename,
        "fileMarkdown": markdown,
        "chunks": chunks,
    }