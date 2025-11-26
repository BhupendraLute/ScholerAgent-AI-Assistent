# tools/pdf_writer.py
from fpdf import FPDF, HTMLMixin
import os
import markdown  # You might need to install this: pip install markdown

class PDF(FPDF, HTMLMixin):
    pass

def create_study_notes_pdf(filename: str, title: str, content: str) -> str:
    """
    Creates a formatted PDF file from Markdown content.
    
    Args:
        filename: The name of the file (e.g., 'notes.pdf').
        title: The title of the document.
        content: The Markdown content (headings, bullets, bold text).
        
    Returns:
        A success message with the file path.
    """
    print(f"\n--- 📄 Generating PDF '{filename}'... ---")
    
    try:
        # 1. Convert Markdown to HTML
        html_content = markdown.markdown(content)
        
        # 2. Initialize PDF
        pdf = PDF()
        pdf.add_page()
        
        # 3. Add Title (Styled)
        pdf.set_font("Helvetica", "", 16)
        pdf.cell(0, 15, title, new_x="LMARGIN", new_y="NEXT", align='C')
        pdf.ln(5)
        
        # 4. Write HTML Content
        pdf.write_html(html_content)
        
        # 5. Save File
        output_dir = "downloads"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            
        # Ensure filename ends in .pdf
        if not filename.endswith('.pdf'):
            filename += ".pdf"
            
        filepath = os.path.join(output_dir, filename)
        pdf.output(filepath)
        
        return f"Success! Formatted PDF saved to {filepath}"
        
    except Exception as e:
        return f"Error creating PDF: {e}"