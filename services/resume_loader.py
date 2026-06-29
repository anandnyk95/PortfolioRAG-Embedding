import pypdf
import os

def load_resume() -> str:
    base_dir = os.path.dirname(os.path.dirname(__file__))
    path = os.path.join(base_dir, "resume", "resume.pdf")
    
    text = ""
    with open(path, "rb") as file:
        reader = pypdf.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    
    return text