from fastapi import FastAPI, File, UploadFile

from api.celery import celery_instance

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Revision AI"}


@app.post("/file-processing")
async def file_processing(file: UploadFile = File(...)):

    filename = file.filename or "upload.bin"  # Fallback filename if none provided   
    content = await file.read()  # Read the file content as bytes
    task = celery_instance.send_task("process_file", args=[file.filename, content])

    return {"message": "File received, processing started", "job_id": task.id, "fileName": filename}


@app.get("/job-status/{job_id}")
def job_status(job_id: str):
    result = celery_instance.AsyncResult(job_id)
    return {"job_id": job_id, "status": result.status, "result": result.result if result.ready() else None}