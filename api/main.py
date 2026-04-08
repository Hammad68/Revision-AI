from fastapi import FastAPI, File, UploadFile

from fastapi.concurrency import run_in_threadpool

from api.processing import convert_document

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Revision AI"}

@app.post("/file-processing")
async def file_processing(file: UploadFile = File(...)):
    data = await file.read()
    markdown, chunks = await run_in_threadpool(convert_document, data, file.filename or "upload.bin")
    return {
        "message": "File Processed",
        "fileName": file.filename,
        "fileMarkdown": markdown,
        "chunks": chunks,
    }