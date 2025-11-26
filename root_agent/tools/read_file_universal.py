from markitdown import MarkItDown

def read_file_universal(file_path):
    """
    Reads PDF, PowerPoint, Word, Excel, Images, and Audio 
    and converts them to LLM-friendly Markdown.
    """
    try:
        md = MarkItDown()
        result = md.convert(file_path)
        return result.text_content
    except Exception as e:
        return f"Error reading file: {str(e)}"
