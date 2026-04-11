from api.celery import celery_instance
from api.processing import convert_document
from docling.document_converter import DocumentConverter
from docling.chunking import HybridChunker

converter = DocumentConverter()
chunker = HybridChunker()

@celery_instance.task(name="process_file")
def process_file(filename: str, content: bytes) -> dict:  
    """Background task to process the uploaded file."""
    try:
        markdown, raw_chunks = convert_document(content, filename, converter, chunker)
        chunks = [chunk.dict() for chunk in raw_chunks]
        return {"message": "File Processed", "fileName": filename, "fileMarkdown": markdown, "chunks": chunks}
    except Exception as e:
        return {"message": "An error occurred during processing", "error": str(e)}