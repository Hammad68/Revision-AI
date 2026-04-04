

def convert_document(file_content: bytes, filename: str) -> str:
    """Convert uploaded file bytes to Markdown. Filename is used for format detection."""
    from io import BytesIO

    from docling.datamodel.base_models import DocumentStream
    
    from docling.document_converter import DocumentConverter

    from docling.chunking.chunker import HybridChunker

    
    buf = BytesIO(file_content)
    source = DocumentStream(name=filename or "upload.bin", stream=buf)
    chunker = HybridChunker()
    chunks = chunker.chunk(source)
    converter = DocumentConverter()
    result = converter.convert(source)
    return result.document.export_to_markdown(), chunks