def convert_document(file_content: bytes, filename: str, converter, chunker) -> tuple:
    """Convert uploaded file bytes to Markdown. Filename is used for format detection."""
    
    from io import BytesIO
    from docling.datamodel.base_models import DocumentStream

    buf = BytesIO(file_content)
    source = DocumentStream(name=filename or "upload.bin", stream=buf)
    
    
    generating_result = converter.convert(source)
    
    dockling_doc = generating_result.document

    markdown = generating_result.document.export_to_markdown()

    chunks = list(chunker.chunk(generating_result.document))

    del generating_result
    
    return markdown, chunks