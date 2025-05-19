import fitz
import os

def pdf_get_text(file_name:str)->str:
    # Create a document object
    doc = fitz.open(filename=file_name)  # or fitz.Document(filename)

    # print(doc.metadata)

    # Get the page by their index
    page = doc.load_page(1)
    # or page = doc[0]   

    # read a Page
    text = page.get_text()
    # print(text)
    return text



def pdftoImg(file_path:str)->str:
    """Extract the pages from the pdfs and return the folder path to where it all stored including the folder name but not any image name like 0.png,1.png etc"""

    ss_folder = "ss"

    doc = fitz.open(filename=f"pdfs/{file_path}")  # or fitz.Document(filename)

    
    # print(doc.page_count)

    if not os.path.exists(os.path.join(ss_folder,file_path)):
        # os.mkdir(f"ss/{file_path}")
        os.mkdir(os.path.join(ss_folder,file_path))

    for i in range(doc.page_count):
        page = doc.load_page(i)
        pix = page.get_pixmap() 
        pix.save(f"{ss_folder}/{file_path}/{page.number}.png")
    
    
    return f"ss/{file_path}"



def get_metadata(file_name):
    doc = fitz.open(filename=file_name)
    #total 11 paramerters
    # print(doc.metadata) 
    return doc.metadata

def normalize_whitespace(s):
    return ' '.join(s.split())


if __name__ == "__main__":
    pdf_get_text()
    get_metadata()
    pdftoImg()
    normalize_whitespace()