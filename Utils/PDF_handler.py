import fitz
import os
import sys

def pdf_to_text(file_name:str)->str:
    # Create a document object
    doc = fitz.open(filename=file_name)  # or fitz.Document(filename)

    content = ""
    # Get the page by their index
    for i in range(doc.page_count):
        page = doc.load_page(i) # or page = doc[0] 
        text = page.get_text() # read a Page
        content = content + normalize_whitespace(text)
     

    return content



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

def cache_pdf(content:str,pdf_name:str)->str:
    """Cache the content of the pdf for the checking with other pdfs helps in
    performance"""

    with open(f"extracted_pdfs/{pdf_name}.txt","w") as f:
        f.write(content)
    
    return f"extracted_pdfs/{pdf_name}.txt"



if __name__ == "__main__":
    pdf_to_text()
    get_metadata()
    pdftoImg()
    normalize_whitespace()
    cache_pdf()    
