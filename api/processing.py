

def convert_document(file_content: bytes, filename: str) -> str:
    """Convert uploaded file bytes to Markdown. Filename is used for format detection."""
    from io import BytesIO

    from docling.datamodel.base_models import DocumentStream
    
    from docling.document_converter import DocumentConverter

    
    buf = BytesIO(file_content)
    source = DocumentStream(name=filename or "upload.bin", stream=buf)
    converter = DocumentConverter()
    generating_result = converter.convert(source)
    dockling_doc = generating_result.document
    markdown = generating_result.document.export_to_markdown()
    return markdown, dockling_doc


def get_chunks(file_obj) -> list[str]:
    """Get chunks from uploaded file bytes."""

    from docling.chunking import HybridChunker

    chunker = HybridChunker()

    chunks = list(chunker.chunk(file_obj))

    return chunks