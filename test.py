import os
from  Utils.OCR import extract_text
from databases.database import DatabaseConn
from Utils.PDF_handler import pdftoImg
import random
from time import sleep
import datetime 



class_id = "class1"
context = "Is this a handwritten? just return 1 or 0"


pdf_files = os.listdir("pdfs")
db = DatabaseConn("databases/PDFS.db")
db.connect()

for pdfs in pdf_files:

    # pdfs = os.path.join("pdfs",pdfs)

    # print(f"Extracting pages from the pdf {pdfs}")
    ss_path =pdftoImg(pdfs)
    # print("Extracted")
    
    print("Getting the response")
    response  = extract_text(f"{ss_path}/0.png")
