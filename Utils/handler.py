# metadata calculations ## Done
# text calculation   
# image calculation ##Done
import os
from Utils.OCR import img_compare,extract_text
from Utils.utilities import util
from Utils.PDF_handler import normalize_whitespace
from time import sleep
from typing import Optional

def compare_pages(file_path1:str,file_path2:str):
    """
    Compares overall pages in PDF and return the similar pages
    based on the two function img_compare and compare_imgratio it returns True if the pdf with the less number of pages is equal to the similar number of pages
    """
    similar_pages =0
    pdf_folder1 =os.listdir(file_path1) 
    pdf_folder2 = os.listdir(file_path2)
    #just provide the folder name and this will return the files availbale in the folder
    img_files1 = sorted(pdf_folder1, key=lambda x: int(x.split('.')[0]))
    img_files2 = sorted(pdf_folder2, key=lambda x: int(x.split('.')[0]))

    for img in img_files1:
        for imgs in img_files2:
            similarity_ratio = img_compare(f"{file_path1}//{img}",f"{file_path2}//{imgs}")
            is_similar = util.compare_imgratio(similarity_ratio)
            if is_similar:
                similar_pages = similar_pages+1
            

    comparable_pdf = len(pdf_folder2) if len(pdf_folder1) > len(pdf_folder2) else len(pdf_folder1) 
                        
    if(comparable_pdf==similar_pages):
        return True
    else:
        return similar_pages


def imgTotext(pdf_name:str)->str:

    """Extract the content from the handwritten pdfs and provides the whole text"""

    img_path= f"ss/{pdf_name}"
    img_dir = os.listdir(img_path)  
    content = ""
    for img in img_dir:
        if os.path.exists(f"{img_path}/{img}"):
            image_text = extract_text(f"{img_path}/{img}")
            # print(image_text)
            # print("*******************************")
            content = content+image_text
            print("Sleeping for 10 secs")
            sleep(10)
        else:
            print("Skipping")
    
    return content

def read_file(file_path:str)-> Optional[str]:   
    
    encodings = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                return f.read()
        except (UnicodeDecodeError, UnicodeError):
            continue
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return None
    
    print(f"Could not read {file_path} with any encoding")
    return False


if __name__ == "__main__":
    read_file()
    imgTotext()
    img_compare()