

converter = None
chunker = None


def convert_document(file_content: bytes, filename: str) -> str:
    """Convert uploaded file bytes to Markdown. Filename is used for format detection."""
    
    global converter

    global chunker
    
    from io import BytesIO

    from docling.datamodel.base_models import DocumentStream
    
    from docling.document_converter import DocumentConverter

    from docling.chunking import HybridChunker

    
    buf = BytesIO(file_content)
    source = DocumentStream(name=filename or "upload.bin", stream=buf)
    
    if converter is None:
        converter = DocumentConverter()
    
    generating_result = converter.convert(source)
    dockling_doc = generating_result.document
    markdown = generating_result.document.export_to_markdown()

    if chunker is None:
        chunker = HybridChunker()

    chunks = list(chunker.chunk(generating_result.document))

    del generating_result
    
    return markdown, chunks


# def get_chunks(file_obj) -> list[str]:
#     """Get chunks from uploaded file bytes."""

#     global chunker

#     from docling.chunking import HybridChunker

#     if chunker is None:
#         chunker = HybridChunker()

#     chunks = list(chunker.chunk(file_obj))

#     return chunks