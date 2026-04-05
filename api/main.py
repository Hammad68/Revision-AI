from fastapi import FastAPI, File, UploadFile

from api.processing import convert_document, get_chunks

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Revision AI"}

@app.post("/file-processing")
async def file_processing(file: UploadFile = File(...)):
    data = await file.read()
    markdown, dockling_doc = convert_document(data, file.filename or "upload.bin")
    chunks = get_chunks(dockling_doc)
    print(markdown)
    print(chunks)
    return {
        "message": "File Processed",
        "fileName": file.filename,
        "fileMarkdown": markdown,
        "chunks": chunks,
    }